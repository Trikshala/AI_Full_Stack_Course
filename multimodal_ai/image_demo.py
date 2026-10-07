import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
    "segmind/tiny-sd",
    torch_dtype=torch.float32
)

image = pipe(
    "A dog eating popcorn in a theatre",
    num_inference_steps=15
).images[0]

image.save("test2.png")

print("Succesful!")