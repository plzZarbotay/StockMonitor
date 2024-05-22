<template>
  <div
    ref="chartContainer"
    style="height: 500px; width: 900px; color: white"
  ></div>
</template>

<script>
import Highcharts from "highcharts";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ChartView",
  computed: {
    ...mapGetters("selected_chart", ["candleData"]),
  },
  mounted() {
    this.fetchAndDisplayCandleData();
  },
  methods: {
    ...mapActions("selected_chart", ["fetchCandleData"]),
    async fetchAndDisplayCandleData() {
      try {
        await this.fetchCandleData();
        this.createChart();
      } catch (error) {
        console.error("Error fetching and displaying candle data:", error);
      }
    },
    createChart() {
      const chartData = this.candleData.slice();

      console.log("Creating chart with data:", chartData);

      if (!Highcharts.stockChart) {
        console.error("Highcharts.stockChart is not available");
        return;
      }

      Highcharts.stockChart(this.$refs.chartContainer, {
        rangeSelector: {
          selected: 1,
        },
        title: {
          text: "TEST Stock Price",
          style: {
            color: "white",
          },
        },
        colors: ["#FF0000", "#00FF00"],
        plotOptions: {
          candlestick: {
            color: "#FF0000",
            upColor: "#00FF00",
            lineColor: "white",
          },
        },
        chart: {
          backgroundColor: null,
        },
        credits: {
          enabled: false,
        },
        xAxis: {
          labels: {
            style: {
              color: "white",
            },
          },
        },
        yAxis: {
          labels: {
            style: {
              color: "white",
            },
          },
        },
        series: [
          {
            type: "candlestick",
            name: "TEST Stock Price",
            data: chartData,
          },
        ],
      });
    },
  },
};
</script>

<style></style>
