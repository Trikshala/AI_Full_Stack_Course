import streamlit as st
import torch
from diffusers import StableDiffusionPipeline
import random

st.set_page_config(page_title="AI Image Generator", page_icon="🎨")
st.title("🎨 AI Image Generator")

@st.cache_resource
def load_model():
    pipe = StableDiffusionPipeline.from_pretrained(
        "segmind/tiny-sd",
        torch_dtype=torch.float32
    )
    return pipe

pipe = load_model()
st.caption("Model loaded!")

st.session_state.setdefault("generated_image", None)
st.session_state.setdefault("generated_prompt", None)
st.session_state.setdefault("image_history", [])

prompt = st.text_input(
    "Describe the image you want:",
    placeholder="a cat wearing sunglasses"
)

generate = st.button("Generate")

if generate and prompt:
    with st.spinner("Generating image... this can take a minute on CPU."):
        image = pipe(prompt, num_inference_steps=8).images[0]

    st.session_state.generated_image = image
    st.session_state.generated_prompt = prompt
    st.session_state.image_history.append({
        "image": image,
        "prompt": prompt
    })
    st.session_state.image_history = st.session_state.image_history[-5:]

# Display the stored image
if st.session_state.generated_image is not None:
    st.image(
        st.session_state.generated_image,
        caption=st.session_state.generated_prompt
    )

if st.session_state.image_history:
    st.subheader("🖼️ Image History")

    for item in reversed(st.session_state.image_history):
        st.image(item["image"], caption=item["prompt"])
    

# Save image
if generate and prompt and st.session_state.generated_image is not None:
    st.session_state.generated_image.save("generated_image.png")
    st.success("Saved as generated_image.png")

sample_prompts = [
    "a futuristic city at sunset",
    "a dog wearing a space helmet",
    "a cozy cabin in the snow",
    "a robot painting on a canvas",
    "a dragon made of glass"
]

if st.button("🎲 Surprise me"):
    st.session_state.surprise_prompt = random.choice(sample_prompts)

if "surprise_prompt" in st.session_state:
    st.info(f"Random prompt: {st.session_state.surprise_prompt}")