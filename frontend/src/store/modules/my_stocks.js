import axios from "axios";

const state = {
  // Your state here
};

const mutations = {
  // Your mutations here
};

const actions = {
  async fetchOwnedStocks({ rootState }) {
    try {
      const response = await axios.get("https://127.0.0.1:8000/api/v1/portfolio/get_owned/", {
        headers: {
          Authorization: `Bearer ${rootState.auth.token}`,
        },
      });
      return response.data;
    } catch (error) {
      console.error("Error fetching owned stocks:", error);
      throw error;
    }
  },
  // Other actions here
};

const getters = {
  // Your getters here
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};
