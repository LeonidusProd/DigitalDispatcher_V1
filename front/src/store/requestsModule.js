import axios from "axios";


export const requestsModule = {
    state: () => ({
        activeRequestId: -1,
        activeSection: 'newRequests',
        requests: [],
        requestTasks: [],
        requestData: {}
    }),
    getters: {},
    mutations: {
        setActiveRequestId(state, pk) {
            state.activeRequestId = pk
        },
        setActiveSection(state, section) {
            state.activeSection = section
        },
        setRequests(state, requests) {
            state.requests = requests
        },
        setRequestTasks(state, requestTasks) {
            state.requestTasks = requestTasks
        },
        setRequestData(state, requestData) {
            state.requestData = requestData
        }
    },
    actions: {
        async loadNewRequests({state, commit}) {
            try {
                const response = (await axios.get('http://localhost:8000/api/v1/requests/new'))
                commit('setRequests', response.data)
            } catch (e) {
                alert('Сервер не доступен')
            }
        },
        async loadActiveRequests({state, commit}) {
            try {
                const response = (await axios.get('http://localhost:8000/api/v1/requests/active'))
                commit('setRequests', response.data)
            } catch (e) {
                alert('Сервер не доступен')
            }
        },
        async loadRequestData({state, commit}, requestId) {
            try {
                const response = (await axios.get(`http://localhost:8000/api/v1/request/${requestId}`))
                commit('setRequestData', response.data)
            } catch (e) {
                alert('Сервер не доступен')
            }
        },
        async loadRequestTasks({state, commit}, requestId) {
            try {
                const response = (await axios.get(`http://localhost:8000/api/v1/request/${requestId}/tasks`))
                commit('setRequestTasks', response.data)
            } catch (e) {
                alert('Сервер не доступен')
            }
        },
    },
    namespaced: true
}