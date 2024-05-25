import axios from "axios";

const state = {
  tableData: [],
};

const mutations = {
  SET_TABLE_DATA(state, data) {
    state.tableData = data;
  },
};

const actions = {
  async fetchStocks({ commit }) {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/v1/market/");
      commit("SET_TABLE_DATA", response.data);
    } catch (error) {
      console.error("Error fetching stocks:", error);
    }
  },
};

const getters = {
  tableData: (state) => state.tableData,
};

export default {
  state,
  mutations,
  actions,
  getters,
};
