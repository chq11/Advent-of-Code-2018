import numpy as np
import torch
import torch.nn as nn

class testNet(nn.Module):
    def __init__(self,k_s):
        super(testNet, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=k_s, stride=1, padding=0, bias=False)
        # for m in self.modules():
        #     if isinstance(m, nn.Linear):
        #         nn.init.constant_(m.weight, 1)
        #         nn.init.constant_(m.bias, -100)
        #     # 也可以判断是否为conv2d，使用相应的初始化方式
        #     elif isinstance(m, nn.Conv2d):
        #         # nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
        #         m.weight.data.fill_(1)
        #
        #     elif isinstance(m, nn.BatchNorm2d):
        #         nn.init.constant_(m.weight.item(), 1)
        #         nn.init.constant_(m.bias.item(), 0)


        # w = torch.from_numpy(np.array([[[[1,2,0],[0,2,1],[0,0,1]]]]))
        torch.nn.init.constant_(self.conv1.weight,1)
    def forward(self, x):
        x = self.conv1(x)
        return x

def main():
    grid = 9424
    ma = np.zeros([300, 300])
    for i in range(300):
        for j in range(300):
            x = i + 1
            y = j + 1
            ma[i, j] = int(((x + 10) * y + grid) * (x + 10) / 100) % 10 - 5
    ma = np.expand_dims(ma, 0)
    ma = np.expand_dims(ma, 1)
    ma = torch.from_numpy(ma).float().cuda()

    max_n = -450000
    x_r, y_r, m_s_r = 0,0,0
    for m_s in range(1,301):
        net = testNet(m_s).cuda()
        outp = net(ma).cpu().detach().numpy()
        outp = outp[0][0]
        dis = np.where(outp == np.max(outp))
        # if dis[0].shape[0] >= 2:
        #     continue
        if outp[dis[0][0], dis[1][0]] > max_n:
            max_n = outp[dis[0][0], dis[1][0]]
            x_r = dis[0][0] + 1
            y_r = dis[1][0] + 1
            m_s_r = m_s
    print(x_r, y_r, m_s_r)


if __name__ == '__main__':
    main()