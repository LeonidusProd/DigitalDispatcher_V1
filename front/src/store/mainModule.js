import axios from "axios";


export const mainModule = {
    state: () => ({
        baseURL: 'http://localhost:8000/api/v1'
    }),
    getters: {},
    mutations: {
        // setActiveSettingsSection(state, section) {
        //     state.activeSettingsSection = section
        // },
    },
    actions: {
        // async loadNewRequests({state, commit}) {
        //     try {
        //         const response = (await axios.get('http://localhost:8000/api/v1/requests/new'))
        //         commit('setRequests', response.data)
        //     } catch (e) {
        //         alert('Сервер не доступен')
        //     }
        // },
        // async createTask({state, commit}, params) {
        //     // console.log('position_pk: ' + params.position_pk)
        //     // console.log('office_pk: ' + params.office_pk)
        //     try {
        //         const response = (
        //             await axios.post('http://localhost:8000/api/v1/task/create', {
        //                 request: params.requestPk,
        //                 employee: params.employeePk,
        //                 service: params.servicePk,
        //                 status: params.status
        //
        //             }, {
        //                 headers: {
        //                     'Content-Type': "application/json"
        //                 }
        //             })
        //         )
        //         commit('setServiceEmployees', response.data)
        //     } catch (e) {
        //         alert('Сервер не доступен')
        //     }
        // },
    },
    namespaced: true
}