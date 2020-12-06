import torch
import time
t1 = time.time()
x = torch.rand(5, 3).cuda()
y = torch.rand(5, 3).cuda()
z = torch.rand(5, 3).cuda()
print(x)
print(time.time()-t1)