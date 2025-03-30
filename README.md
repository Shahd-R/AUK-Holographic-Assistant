# AUK-Holographic-Assistant
AUK Holographic assistant is an AI-chatbot with verbal input and output, with the ouput spoken by a 3D model designed on Blender.

--Program Installation--

- Download Python 3.12 and set the system interpreter in Visual Studio Code as Python 3.12.
- Set up a virtual environment, also using Python 3.12.
- "run_llama.py" is the full program file.
- Install, using pip or otherwise:

  - llama.cpp
  - portaudio
  - elevenlabs   (https://github.com/elevenlabs/elevenlabs-python)
  - RealTimeSTT  (https://github.com/KoljaB/RealtimeSTT)
-    # Load the Llama model
    llm = Llama(model_path="/Users/nadaremah/Documents/llama-code/unsloth.Q8_0.gguf")
  Change it to be your path for the where the model is installed on your system

-    # Change the def __init__ in audio.recorder.py
    def __init__(self,
                 model: str = "small",# INIT_MODEL_TRANSCRIPTION,
                 download_root: str = None, 
                 language: str = "en",
                 compute_type: str = "default",
                 input_device_index: int = None,
                 gpu_device_index: Union[int, List[int]] = 0,
                 device: str = "cuda",
                 on_recording_start=None,
                 on_recording_stop=None,
                 on_transcription_start=None,
                 ensure_sentence_starting_uppercase=True,
                 ensure_sentence_ends_with_period=True,
                 use_microphone=True,
                 spinner=True,
                 level=logging.WARNING,
                 batch_size: int = 16,

                 # Realtime transcription parameters
                 enable_realtime_transcription=True,
                 use_main_model_for_realtime=False,
                 realtime_model_type=INIT_MODEL_TRANSCRIPTION_REALTIME,
                 realtime_processing_pause=INIT_REALTIME_PROCESSING_PAUSE,
                 init_realtime_after_seconds=INIT_REALTIME_INITIAL_PAUSE,
                 on_realtime_transcription_update=None,
                 on_realtime_transcription_stabilized=None,
                 realtime_batch_size: int = 16,

                 # Voice activation parameters
                 silero_sensitivity: float = 0.8,#INIT_SILERO_SENSITIVITY,
                 silero_use_onnx: bool = False,
                 silero_deactivity_detection: bool = False,
                 webrtc_sensitivity: int = INIT_WEBRTC_SENSITIVITY,
                 post_speech_silence_duration: float = 0.5,#(
                    # INIT_POST_SPEECH_SILENCE_DURATION
                 #),
                 min_length_of_recording: float = 3.0,#(
                     #INIT_MIN_LENGTH_OF_RECORDING
                 #),
                 min_gap_between_recordings: float = 2.0,#(
                     #INIT_MIN_GAP_BETWEEN_RECORDINGS
                 #),
                 pre_recording_buffer_duration: float = (
                     INIT_PRE_RECORDING_BUFFER_DURATION
                 ),
                 on_vad_detect_start=None,
                 on_vad_detect_stop=None,

                 # Wake word parameters
                 wakeword_backend: str = "oww",
                 openwakeword_model_paths: str = '/Users/nadaremah/Documents/llama-code/Hellow_wolfy!.onnx',
                 openwakeword_inference_framework: str = "onnx",
                 wake_words: str = "",
                 wake_words_sensitivity: float = INIT_WAKE_WORDS_SENSITIVITY,
                 wake_word_activation_delay: float = (
                    INIT_WAKE_WORD_ACTIVATION_DELAY
                 ),
                 wake_word_timeout: float = 5,  #INIT_WAKE_WORD_TIMEOUT,
                 wake_word_buffer_duration: float = 0.7,#INIT_WAKE_WORD_BUFFER_DURATION,
                 on_wakeword_detected=None,
                 on_wakeword_timeout=None,
                 on_wakeword_detection_start=None,
                 on_wakeword_detection_end=None,
                 on_recorded_chunk=None,
                 debug_mode=True,
                 handle_buffer_overflow: bool = INIT_HANDLE_BUFFER_OVERFLOW,
                 beam_size: int = 5,
                 beam_size_realtime: int = 3,
                 buffer_size: int = BUFFER_SIZE,
                 sample_rate: int = SAMPLE_RATE,
                 initial_prompt: Optional[Union[str, Iterable[int]]] = None,
                 initial_prompt_realtime: Optional[Union[str, Iterable[int]]] = None,
                 suppress_tokens: Optional[List[int]] = [-1],
                 print_transcription_time: bool = False,
                 early_transcription_on_silence: int = 0,
                 allowed_latency_limit: int = ALLOWED_LATENCY_LIMIT,
                 no_log_file: bool = False,
                 use_extended_logging: bool = False,
                 ):

Note: If it gives n error that it cant get the AI voice from the internet, go to your Python 3.12 folder and run "Install Certificates.command"

and that should be it, i hope.
