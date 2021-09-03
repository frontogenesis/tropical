import tropycal.realtime as realtime
import warnings

warnings.filterwarnings('ignore', category=UserWarning)

data = realtime.Realtime()
storms_list = data.list_active_storms()

def choose_basin(basin='AL'):
    '''Returns Atlantic (AL) or Eastern Pacific (EP) storms'''
    storm_metadata = []

    if basin.upper() != 'AL' and basin.upper() != 'EP':
        raise ValueError('Specify AL to return Atlantic Basin storms or EP for Eastern Pacific storms')

    if basin.upper() == 'AL' or basin.upper() == 'EP':
        filtered_list = [storm for storm in storms_list if storm[:2].upper() == basin.upper()]

        for storm in filtered_list:
            storm_metadata.append(data.get_storm(storm))

    return storm_metadata


def plot_cones():
    '''Generate forecast cone graphics'''
    storms = choose_basin()

    for storm in storms:
        storm.plot_forecast_realtime(save_path='', track_labels='valid_edt', return_ax=True)

def main():
    if not storms_list:
        return
    plot_cones()
        

if __name__ == '__main__':
    main()