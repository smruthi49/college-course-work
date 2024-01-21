## Time Series Analysis

The dataset contains temperature readings inside and outside of a room. The data is from Jan 2018 to Nov 2018.\
The device which measures the temperature was shut down several times using the entire period 28-07-2018 to 08-12-2018.\
We have 5 columns.
- id (unique ID for readings)
- room_id/id (room in which device was installed)
- noted_date (date and time of the reading)
- temp (temperature reading)
- out/in (reading taken inside or outside)

Observations are made based on the place, timing, months, seasons, hours.

However, the predictions are not upto mark as :
- The data available was insufficent
- The data had multiple temperatures in the same day at differnt times. But we took into account only everyday values.
- The null values were filled by us.
