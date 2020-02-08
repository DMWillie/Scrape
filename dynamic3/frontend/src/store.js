import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    url: {
      index: '/api/movie',
      detail: '/api/movie/{id}'
    }
  },
  mutations: {

  },
  actions: {

  }
})
