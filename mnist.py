import torchvision
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--result-path', default='./')
args = parser.parse_args()

train_data = torchvision.datasets.MNIST(args.result_path, train=True, transform=None, target_transform=None, download=True)
test_data  = torchvision.datasets.MNIST(args.result_path, train=False, transform=None, target_transform=None, download=True)
print(len(train_data), len(test_data))
