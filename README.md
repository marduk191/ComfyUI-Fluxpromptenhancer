# Flux Prompt Enhance Node for ComfyUI

This custom node for ComfyUI integrates the Flux-Prompt-Enhance model, allowing you to enhance your prompts directly within your ComfyUI workflows.

## Features

- Enhance short prompts into more detailed, descriptive ones suited for flux.1
- Token limited to 256 for compatibility with schnell.
- Seamless integration with ComfyUI
- Easy to install and use

## Installation

1. Ensure you have ComfyUI installed and working.

2. Clone this repository into your ComfyUI custom nodes directory:

   ```
   cd /path/to/ComfyUI/custom_nodes
   git clone https://github.com/yourusername/comfyui-flux-prompt-enhance.git
   ```

3. Install the required dependencies:

   ```
   cd comfyui-flux-prompt-enhance
   pip install -r requirements.txt
   ```

   Note: Make sure you're using the same Python environment that ComfyUI uses.

4. Install the Flux-Prompt-Enhance model:
   
   The model will be automatically downloaded from huggingface when you first use the node. 
  
5. Restart ComfyUI or reload custom nodes.

## Usage

1. In the ComfyUI interface, you should now see a new node called "Flux Prompt Enhance" in the "marduk191/Flux_Promt_Enhance" category.

2. Connect a string input (your initial prompt) to this node.

3. The node will output an enhanced version of your input prompt.

## Example

Input: "beautiful house with text 'hello'"

Output: "a two-story house with white trim, large windows on the second floor, three chimneys on the roof, green trees and shrubs in front of the house, stone pathway leading to the front door, text on the house reads "hello" in all caps, blue sky above, shadows cast by the trees, sunlight creating contrast on the house's facade, some plants visible near the bottom right corner, overall warm and serene atmosphere."

## Troubleshooting

- If the node doesn't appear in ComfyUI, make sure you've placed the files in the correct directory and restarted ComfyUI.
- If you encounter any "module not found" errors, ensure that all dependencies are correctly installed in the same Python environment that ComfyUI is using.
- If you get an error about the model not being found, make sure you have an internet connection for the automatic download, or try the manual download step in the installation instructions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This node uses the [Flux-Prompt-Enhance](https://huggingface.co/gokaygokay/Flux-Prompt-Enhance) model by gokaygokay.
- Thanks to the ComfyUI team for creating an extensible platform.

