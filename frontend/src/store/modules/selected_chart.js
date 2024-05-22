import axios from "axios";
import Highcharts from "highcharts";
import StockModule from "highcharts/modules/stock";
import AnnotationsModule from "highcharts/modules/annotations";

StockModule(Highcharts);
AnnotationsModule(Highcharts);

const state = {
  candleData: [],
};

const getters = {
  candleData: (state) => state.candleData,
};

const mutations = {
  setCandleData(state, data) {
    state.candleData = data;
  },
};

const actions = {
  async fetchCandleData({ commit }) {
    try {
      const currentDate = new Date();
      const fromDate = new Date(
        currentDate.setFullYear(currentDate.getFullYear() - 1)
      ).toISOString();
      const toDate = new Date().toISOString();

      const response = await axios.post(
        "http://127.0.0.1:8000/api/v1/market/YNDX/candles/",
        {
          from_date: fromDate,
          till_date: toDate,
          interval: 5,
        }
      );

      const candleData = response.data.map((candle) => [
        new Date(candle.begin).getTime(),
        parseFloat(candle.open_cost),
        parseFloat(candle.high),
        parseFloat(candle.low),
        parseFloat(candle.close_cost),
      ]);

      console.log("Fetched candle data:", candleData);

      commit("setCandleData", candleData);
    } catch (error) {
      console.error("Error fetching candle data:", error);
    }
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
