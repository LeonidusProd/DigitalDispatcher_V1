import axios from "axios";


export const requestsModuleOld = {
    state: () => ({
        activeRequestId: -1,
        // activeSection: 'newRequests',
        // requests: [],
        requestTasks: [],
        requestData: {},
        taskListKey: 0,
        standartServices: [],
        serviceEmployees: [],
    }),
    getters: {},
    mutations: {
        setActiveRequestId(state, pk) {
            state.activeRequestId = pk
        },
        // setActiveSection(state, section) {
        //     state.activeSection = section
        // },
        // setRequests(state, requests) {
        //     state.requests = requests
        // },
        setRequestTasks(state, requestTasks) {
            state.requestTasks = requestTasks
        },
        setRequestData(state, requestData) {
            state.requestData = requestData
        },
        setTaskListKey(state, taskListKey) {
            state.taskListKey = taskListKey
        },
        setStandartServices(state, standartServices) {
            state.standartServices = standartServices
        },
        setServiceEmployees(state, serviceEmployees) {
            state.serviceEmployees = serviceEmployees
        },
    },
    actions: {
        // async loadRequestData({state, commit}, requestId) {
        //     try {
        //         const response = (await axios.get(
        //             `http://localhost:8000/api/v1/request/${requestId}`,
        //             {
        //                 headers: {
        //                     'Authorization': `Token ${localStorage.getItem('auth_token')}`
        //                 }
        //             }
        //         ))
        //         commit('setRequestData', response.data)
        //     } catch (e) {
        //         alert('Сервер не доступен')
        //     }
        // },
        // async loadRequestTasks({state, commit}, requestId) {
        //     try {
        //         const response = (await axios.get(
        //             `http://localhost:8000/api/v1/request/${requestId}/tasks`,
        //             {
        //                 headers: {
        //                     'Authorization': `Token ${localStorage.getItem('auth_token')}`
        //                 }
        //             }
        //         ))
        //         commit('setRequestTasks', response.data)
        //     } catch (e) {
        //         alert('Сервер не доступен')
        //     }
        // },
        // async loadStandartServices({state, commit}) {
        //     try {
        //         const response = (await axios.get(
        //             'http://localhost:8000/api/v1/service/',
        //             {
        //                 headers: {
        //                     'Authorization': `Token ${localStorage.getItem('auth_token')}`
        //                 }
        //             }
        //         ))
        //         commit('setStandartServices', response.data)
        //     } catch (e) {
        //         alert('Сервер не доступен')
        //     }
        // },
        // async loadServiceEmployees({state, commit}, params) {
        //     // console.log('position_pk: ' + params.position_pk)
        //     // console.log('office_pk: ' + params.office_pk)
        //     try {
        //         const response = (
        //             await axios.get(
        //                 'http://localhost:8000/api/v1/service/employees/',
        //                 {
        //                     params: {
        //                         'position_pk': params.position_pk,
        //                         'office_pk': params.office_pk
        //                     },
        //                     headers: {
        //                         'Authorization': `Token ${localStorage.getItem('auth_token')}`
        //                     }
        //                 })
        //         )
        //         commit('setServiceEmployees', response.data)
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
        //                     'Content-Type': "application/json",
        //                     'Authorization': `Token ${localStorage.getItem('auth_token')}`
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