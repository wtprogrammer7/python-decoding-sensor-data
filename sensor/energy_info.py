from house_info import HouseInfo

class EnergyData(HouseInfo):
    ENERGY_PER_BULB = 0.2
    ENERGY_BITS = 0x0F0
    def _get_energy(self, rec):
        energy = int(rec, base=16)
        energy = energy & self.ENERGY_BITS # mask ENERGY bits
        energy = energy >> 4 # shift right
        return energy

    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(self._get_energy(rec))
        return recs