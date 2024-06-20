synapses:
  - name: "adsanalog"
    signals:
      - order: "read-analog-0"
    neurons:
      - ads1115_analog:
          readChannel: ADS.P0
         
- name: "adsanalog"
    signals:
      - order: "read-analog-1"
    neurons:
      - ads1115_analog:
          readChannel: ADS.P1

- name: "adsanalog"
    signals:
      - order: "read-analog-2"
    neurons:
      - ads1115_analog:
          readChannel: ADS.P2

- name: "adsanalog"
    signals:
      - order: "read-analog-3"
    neurons:
      - ads1115_analog:
          readChannel: ADS.P3