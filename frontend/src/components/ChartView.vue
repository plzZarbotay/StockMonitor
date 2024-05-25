<template>
  <div>
    <div
      ref="chartContainer"
      style="height: 500px; width: 1000px; color: white"
    ></div>
    <div style="margin-bottom: 20px; color: white">
      <label style="color: #42b983">
        <input type="checkbox" v-model="showSMA" @change="createChart" />
        Скользящее среднее (SMA)
      </label>
      <label style="color: #42b983">
        <input
          type="checkbox"
          v-model="showBollingerBands"
          @change="createChart"
          style="background-color: rgba(10, 20, 41, 1)"
        />
        Линии Боллинджера
      </label>
    </div>
  </div>
</template>

<script>
import Highcharts from "highcharts";
import StockModule from "highcharts/modules/stock";
import AnnotationsModule from "highcharts/modules/annotations";
import IndicatorsModule from "highcharts/indicators/indicators";
import BollingerBands from "highcharts/indicators/bollinger-bands";
import { mapGetters, mapActions } from "vuex";

// Инициализация модулей
StockModule(Highcharts);
AnnotationsModule(Highcharts);
IndicatorsModule(Highcharts);
BollingerBands(Highcharts);

export default {
  name: "ChartView",
  data() {
    return {
      showSMA: false,
      showBollingerBands: false,
    };
  },
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
    calculateSMA(data, period) {
      let sum = 0;
      return data.map((value, index) => {
        sum += value[4]; // Закрытие цены
        if (index >= period) {
          sum -= data[index - period][4];
          return [value[0], sum / period];
        }
        return [value[0], null];
      });
    },
    createChart() {
      const chartData = this.candleData.slice();

      console.log("Creating chart with data:", chartData);

      if (!Highcharts.stockChart) {
        console.error("Highcharts.stockChart is not available");
        return;
      }

      const smaData = this.calculateSMA(chartData, 14); // Скользящая средняя за 14 периодов

      const series = [
        {
          type: "candlestick",
          //name: "TEST Stock Price",
          id: "candlestick",
          data: chartData,
        },
      ];

      if (this.showSMA) {
        series.push({
          type: "line",
          name: "SMA (14)",
          data: smaData,
          color: "#0000FF",
          tooltip: {
            valueDecimals: 2,
          },
        });
      }

      if (this.showBollingerBands) {
        series.push({
          type: "bb",
          name: "Bollinger Bands",
          linkedTo: "candlestick",
          color: "#FFFF00",
          params: {
            period: 20,
            standardDeviation: 2,
          },
        });
      }

      Highcharts.stockChart(this.$refs.chartContainer, {
        rangeSelector: {
          buttons: [
            {
              type: "day",
              count: 1,
              text: "1d",
            },
            {
              type: "day",
              count: 3,
              text: "3d",
            },
            {
              type: "month",
              count: 1,
              text: "1m",
            },
            {
              type: "month",
              count: 3,
              text: "3m",
            },
            {
              type: "year",
              count: 1,
              text: "1y",
            },
          ],
          selected: 2, // Default selection
        },
        title: {
          text: "",
          style: {
            color: "white",
          },
        },
        colors: ["#FF0000", "#00FF00", "#0000FF", "#FFFF00"],
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
        series: series,
      });
    },
  },
};
</script>

<style></style>
