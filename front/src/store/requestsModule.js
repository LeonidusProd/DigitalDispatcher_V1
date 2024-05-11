import axios from "axios";


export const requestsModuleOld = {
    state: () => ({
        activeRequestId: -1,

    }),
    getters: {},
    mutations: {
        setActiveRequestId(state, pk) {
            state.activeRequestId = pk
        },
    },
    actions: {},
    namespaced: true
}