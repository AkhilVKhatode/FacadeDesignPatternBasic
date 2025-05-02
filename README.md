# Multimedia App

This is a simple Python-based multimedia app that allows users to play music, play video, or view an image using a facade design pattern. The app provides a unified interface to interact with different media types (audio, video, image) through the `MediaFacade` class.

## Classes Overview

- **MusicPlayer**: Handles the initialization of audio drivers, audio decoding, and music playback.
- **VideoPlayer**: Manages the setup of rendering engines, video file loading, and video playback.
- **ImageViewer**: Responsible for loading image files, scaling the image, and displaying it.
- **MediaFacade**: Acts as a facade to provide a simplified interface for the user to perform actions (e.g., play music, play video, view image) without interacting with the individual media player classes directly.

## How It Works

1. **User Input**: The user is prompted to choose an action from the following options:
   - `playMusic`: Initializes audio drivers, decodes the audio, and starts music playback.
   - `playVideo`: Sets up the rendering engine, loads a video file, and starts video playback.
   - `viewImage`: Loads an image file, applies scaling, and displays the image.

2. **Facade Design Pattern**: The `MediaFacade` class acts as a gateway to the underlying media classes (`MusicPlayer`, `VideoPlayer`, and `ImageViewer`), simplifying the interaction for the user.

### Example:
```
Welcome to Multimedia App!
Choose an action: playMusic, playVideo, viewImage
playMusic
Audio drivers initialized.
Audio decoded.
Music playback started.
```
