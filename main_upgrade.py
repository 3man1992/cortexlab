import utils as util
import time
import chart_generation as charts
import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plt
import pandas as pd

# pd.set_option('display.max_columns', None)  # or 1000
# pd.set_option('display.max_rows', None)  # or 1000
# pd.set_option('display.max_colwidth', None)  # or 199

#Performance checks
start_time = time.time()

#Load the data - computes: self.trial_df, spike_df, brain_regions
data = util.Upload_Data(session_data = '/Users/laurencefreeman/Documents/thesis_data/processed_physdata_v1/aligned_physdata_KM011_2020-03-23_probe1.mat',
                        frame_alignment_data = '/Users/laurencefreeman/Documents/thesis_data/KM011_video_timestamps/2020-03-23/face_timeStamps.mat',
                        dlc_video_csv = '/Users/laurencefreeman/Documents/thesis_data/23_faceDLC_resnet50_Master_ProjectAug13shuffle1_133500.csv')

#Single PSTH
# charts.generate_PSTH(data.trial_df, data.spike_df, 23)

raster_object = charts.Raster(data.trial_df,
                              data.spike_df,
                              data.first_lick_df,
                              data.brain_regions)

#Single raster for testing
# fig = raster_object.gen_event_plot(2)

# Multiple viz gen
pdf = matplotlib.backends.backend_pdf.PdfPages("rasters_ranked.pdf")
for x in range(100):
    fig = raster_object.gen_event_plot(x)
    pdf.savefig(fig)
    plt.close(fig)
    print("Raster completed")
pdf.close()

#How long did the full script take?
print("")
print("--- %s seconds ---" % (time.time() - start_time))
print("")
