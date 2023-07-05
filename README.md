# Machine-Vision-Painting
# Virtual Paint

This project allows you to create a virtual paint program using your webcam and hand gestures. You can draw on the screen by moving your hand and select different colors and brush thickness using hand gestures.

## Requirements
- Python 3.x
- OpenCV
- NumPy
- HandModule (custom module included in the repository)

## Installation
1. Clone the repository to your local machine.
2. Install the required dependencies using pip:
3. Run the main script:

## Usage
1. Launch the script, and it will open your webcam feed along with a GUI window.
2. Place your hand in front of the webcam.
3. Move your index finger up and down to adjust the brush thickness.
4. Move your hand to the predefined color zones to change the brush color.
5. To draw, close your thumb and index finger together, and move your hand.
6. To erase the drawing, open your hand completely or swing your hand.

## File Structure
- `virtual_paint.py`: The main script that captures the webcam feed, detects hand gestures, and handles the drawing logic.
- `HandModule.py`: A custom module that provides hand detection and tracking functionalities.
- `toolbar/`: A directory containing toolbar images for selecting colors and brush thickness.



