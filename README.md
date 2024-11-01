No longer maintained for public updates as another developer has started a version and we really don't need 2.

# Flux Prompt Enhance Node for ComfyUI

This custom node for ComfyUI integrates the Flux-Prompt-Enhance model, allowing you to enhance your prompts directly within your ComfyUI workflows.

## Features

- Enhance short prompts into more detailed, descriptive ones
- Seamless integration with ComfyUI
- Token limited to 256 for schnell compatibility
- Easy to install and use

## Prerequisites

- ComfyUI installed and working
- Python 3.7 or higher
- PyTorch 1.9.0 or higher
- Hugging Face Transformers library 4.18.0 or higher

## Installation

1. Ensure you have ComfyUI installed and working.

2. Clone this repository into your ComfyUI custom nodes directory:

   ```
   cd /path/to/ComfyUI/custom_nodes
   git clone https://github.com/marduk191/ComfyUI-Fluxpromptenhancer.git
   ```

3. Install the required dependencies:

   ```
   cd ComfyUI-Fluxpromptenhancer
   pip install -r requirements.txt
   ```

   This will install PyTorch and the Hugging Face Transformers library, along with any other necessary dependencies.

   Note: Make sure you're using the same Python environment that ComfyUI uses.

4. The Flux-Prompt-Enhance model will be automatically downloaded when you first use the node. However, if you want to pre-download it or if you're working in an offline environment, you can manually download the model:

   ```
   python -c "from transformers import AutoTokenizer, AutoModelForSeq2SeqLM; AutoTokenizer.from_pretrained('gokaygokay/Flux-Prompt-Enhance'); AutoModelForSeq2SeqLM.from_pretrained('gokaygokay/Flux-Prompt-Enhance')"
   ```

   This command will download the model and tokenizer to the default Hugging Face cache directory (usually `~/.cache/huggingface/` on Linux or `C:\Users\YourUsername\.cache\huggingface\` on Windows).

5. Restart ComfyUI or reload custom nodes.

## Usage

1. In the ComfyUI interface, you should now see a new node called "Flux Prompt Enhance" in the "marduk191/Flux_Prompt_Enhancer" category.

2. You can type in this node, or convert the widget to input and connect a string input (your initial prompt) to this node.

3. The node will output an enhanced version of your input prompt.

## Example

Input: "beautiful house with text 'hello'"

Output: "a two-story house with white trim, large windows on the second floor, three chimneys on the roof, green trees and shrubs in front of the house, stone pathway leading to the front door, text on the house reads "hello" in all caps, blue sky above, shadows cast by the trees, sunlight creating contrast on the house's facade, some plants visible near the bottom right corner, overall warm and serene atmosphere."

## Troubleshooting

- If the node doesn't appear in ComfyUI, make sure you've placed the files in the correct directory and restarted ComfyUI.
- If you encounter any "module not found" errors, ensure that all dependencies (including PyTorch and Hugging Face Transformers) are correctly installed in the same Python environment that ComfyUI is using.
- If you get an error about the model not being found, make sure you have an internet connection for the automatic download, or try the manual download step in the installation instructions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This node uses the [Flux-Prompt-Enhance](https://huggingface.co/gokaygokay/Flux-Prompt-Enhance) model by gokaygokay.
- Thanks to the ComfyUI team for creating an extensible platform.
- This project relies on the Hugging Face Transformers library for model loading and inference.

