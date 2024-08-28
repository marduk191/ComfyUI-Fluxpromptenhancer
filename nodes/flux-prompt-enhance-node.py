import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

class FluxPromptEnhanceNode:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_checkpoint = "gokaygokay/Flux-Prompt-Enhance"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_checkpoint)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_checkpoint)
        self.enhancer = pipeline('text2text-generation',
                                 model=self.model,
                                 tokenizer=self.tokenizer,
                                 repetition_penalty=1.2,
                                 device=self.device)
        self.max_target_length = 256
        self.prefix = "enhance prompt: "

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "enhance_prompt"
    CATEGORY = "marduk191/Flux_Prompt_Enhancer"

    def enhance_prompt(self, prompt):
        answer = self.enhancer(self.prefix + prompt, max_length=self.max_target_length)
        enhanced_prompt = answer[0]['generated_text']
        return (enhanced_prompt,)

NODE_CLASS_MAPPINGS = {
    "FluxPromptEnhance": FluxPromptEnhanceNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FluxPromptEnhance": "Flux Prompt Enhance"
}
