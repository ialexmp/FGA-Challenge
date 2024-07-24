class VGGSimple5(nn.Module):
    def __init__(self, num_classes=10):

        super(VGGSimple5, self).__init__()

        self.conv11 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1)
        self.conv12 = nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1)
        self.conv13 = nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1)

        self.conv20 = nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1)
        self.conv21 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
        self.conv22 = nn.Conv2d(128,128, kernel_size=3, stride=1, padding=1)

        self.maxpool = nn.MaxPool2d(kernel_size=5, stride=5)

        self.fc1 = nn.Linear(8*8*128, 80)
        self.fc2 = nn.Linear(80, num_classes)

        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.15)

    def forward(self, x):

        out = self.relu(self.conv11(x))
        out = self.relu(self.conv12(out))
        out = self.relu(self.conv13(out))
        out = self.maxpool(out)
        out = self.dropout(out)

        out = self.relu(self.conv20(out))
        out = self.relu(self.conv21(out))
        out = self.relu(self.conv22(out))
        out = self.maxpool(out)
        out = self.dropout(out)

        out = out.view(out.size(0), -1)
        out = self.fc1(out)
        out = self.dropout(out)
        out = self.fc2(out)

        return out
