import time

import gpulink as gpu

with gpu.NVContext() as ctx:

    print(f"Available GPUs: {ctx.gpus}")
    print(f"Single Memory Info query: {ctx.get_memory_info(ctx.gpus)}")

    recorder = gpu.Recorder.create_memory_recorder(ctx, ctx.gpus)
    recorder.start()
    time.sleep(3)  # Record for 3 seconds
    recorder.stop(auto_join=True)

    recording = recorder.get_recording()
    print(recording)

    gpu.Plot(recording).plot(scale_y_axis=True)
