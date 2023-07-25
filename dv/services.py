# Imports
import torch
import torchaudio
import os
import gc

from tortoise.utils.audio import load_voices

def text_to_speech(
    tortoise_instance,
    text,
    emotion,
    voice_dirs,
    results_dir,
    regenerate=False,
):
    if not os.path.exists(results_dir):
        os.mkdir(results_dir)

    tts_sentence = f"[I am so {emotion}] {text}"

    voice_samples, conditioning_latents = load_voices(voice_dirs)

    # presets = {
    #     'ultra_fast': {'num_autoregressive_samples': 16, 'diffusion_iterations': 30, 'cond_free': False},
    #     'fast': {'num_autoregressive_samples': 96, 'diffusion_iterations': 80},
    #     'standard': {'num_autoregressive_samples': 256, 'diffusion_iterations': 200},
    #     'high_quality': {'num_autoregressive_samples': 256, 'diffusion_iterations': 400},
    # }
    preset = "high_quality"

    generated_audio = tortoise_instance.tts_with_preset(
        tts_sentence,
        results_dir=results_dir,
        regenerate=regenerate,
        voice_samples=voice_samples,
        conditioning_latents=conditioning_latents,
        preset=preset,
    )

    torchaudio.save(results_dir, generated_audio.squeeze(0).cpu(), 24000)

    # empty cache to solve memory issues
    torch.cuda.empty_cache()
    gc.collect()
