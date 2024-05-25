// store/modules/search_stocks.js

import axios from "axios";

const state = {
  searchResults: [],
};

const mutations = {
  SET_SEARCH_RESULTS(state, results) {
    state.searchResults = results;
  },
};

const actions = {
  async fetchSearchResults({ commit }, query) {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/v1/market/`, {
        params: { q: query },
      });
      commit("SET_SEARCH_RESULTS", response.data);
    } catch (error) {
      console.error("Error fetching search results:", error);
    }
  },
};

const getters = {
  searchResults: (state) => state.searchResults.slice(0, 5),
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};
