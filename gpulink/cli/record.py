from pathlib import Path
from typing import Optional

from matplotlib import pyplot as plt

from gpulink import DeviceCtx, Plot, Recorder
from gpulink.cli.tools import start_in_background
from gpulink.recording.gpu_recording import Recording


def _check_output_file_type(output_path: Path):
    supported_file_types = plt.gcf().canvas.get_supported_filetypes()
    # Necessary to ensure that implicitly created figure is deleted
    plt.clf()
    plt.cla()
    plt.close()
    if output_path and output_path.suffix[1:] not in supported_file_types:
        raise ValueError(f"Output format '{output_path.suffix}' not supported")


def _store_records(recording: Recording, output_path: Optional[Path]):
    if output_path:
        graph = Plot(recording)
        graph.save(output_path)


def _display_plot(recording: Recording, args):
    if args.plot:
        recording.plot_options.auto_scale = args.autoscale
        p = Plot(recording)
        p.plot()


def record(args):
    """Record GPU properties"""

    _check_output_file_type(args.output)

    with DeviceCtx() as ctx:
        recorder = Recorder.create_memory_recorder(ctx, ctx.gpus.ids)
        start_in_background(recorder, "[RECORDING]")
        recording = recorder.get_recording()

    print(recording)

    _store_records(recording, args.output)
    _display_plot(recording, args)
