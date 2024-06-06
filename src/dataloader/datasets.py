from torch.utils.data import Dataset, DataLoader


class SlidingWindowDataset(Dataset):
    """
        Sliding Window: A sliding window moves by a fixed amount after each step,
    often by the size of the window itself. This means that there is no overlap between
    the data in consecutive windows. This approach is useful when you want to prevent data points
    from being included in the calculation more than once, which could skew the results.
    """

    def __init__(self, data, window_size):
        self.data = data
        self.window_size = window_size

    def __len__(self):
        return max(0, len(self.data) - self.window_size + 1)

    # TODO: Fix this

    def __getitem__(self, idx):
        window_data = self.data[idx : idx + self.window_size]
        window_label = self.data[idx + self.window_size + 1]
        return window_data, window_label


class OverlappingWindowDataset(Dataset):
    """
       Overlapping Window: An overlapping window moves by a smaller step, meaning that
    consecutive windows share some of the same data points. This approach can be useful
    when you want to smooth out fluctuations in the data, as each data point will contribute
    to several windows. It can also help to capture patterns that might be missed if they
    fall on the boundary between two non-overlapping windows
    """

    def __init__(self, data, window_size, overlap=1):
        self.data = data
        self.window_size = window_size
        self.overlap = overlap

    def __len__(self):
        return max(0, len(self.data) - self.window_size + 1)

    # TODO: Fix this

    def __getitem__(self, idx):
        window_data = self.data[idx : idx + self.window_size]
        window_label = self.data[idx + self.window_size]
        return window_data, window_label


def get_dataloader(
    dataset,
    batch_size,
):
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=False)
    return dataloader
