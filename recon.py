import tropycal.recon as recon
from collections import namedtuple

Storm = namedtuple("Storm", "name year")
storm = Storm("Ida", 2021)

recon_data = recon.ReconDataset(storm)

print(recon_data)