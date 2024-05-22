import { createStore } from "vuex";
//import axios from "axios";
import auth from "./modules/auth";
import selected_chart from "./modules/selected_chart";

export default createStore({
  modules: {
    auth,
    selected_chart,
  },
});
