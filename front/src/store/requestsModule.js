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
        setActiveRequestId(state, id) {
            state.activeRequestId = id
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
            commit(
                'setRequests',
                [
                    {
                        id: 1,
                        date: '23.04.2024 16:00',
                        adress: 'Ул. Пупина, д. 13',
                        info: '1. Нет света',
                        status: 'Новая',
                        resident: 'Житель 1'
                    },
                    {
                        id: 2,
                        date: '23.04.2024 14:20',
                        adress: 'Ул. Волжская, д. 74',
                        info: '2. Разбитое стекло в 3 подьезде',
                        status: 'Новая',
                        resident: 'Житель 2'
                    },
                    {
                        id: 3,
                        date: '23.04.2024 13:10',
                        adress: 'Ул. Борская, д. 18',
                        info: '3. Протекает полотенцесушитель',
                        status: 'Новая',
                        resident: 'Житель 3'
                    },
                    {
                        id: 4,
                        date: '23.04.2024 12:50',
                        adress: 'Ул. Окская, д. 20',
                        info: '4. Переполнены мусорные баки',
                        status: 'Новая',
                        resident: 'Житель 4'
                    },
                ]
            )
        },
        async loadActiveRequests({state, commit}) {
            commit(
                'setRequests',
                [
                    {
                        id: 5,
                        date: '23.04.2024 12:50',
                        adress: 'Ул. Окская, д. 20',
                        info: '5. Переполнены мусорные баки',
                        status: 'В работе',
                        resident: 'Житель 5'
                    },
                    {
                        id: 6,
                        date: '23.04.2024 12:50',
                        adress: 'Ул. Окская, д. 20',
                        info: '6 .Переполнены мусорные баки',
                        status: 'В работе',
                        resident: 'Житель 6'
                    },
                    {
                        id: 7,
                        date: '23.04.2024 12:50',
                        adress: 'Ул. Окская, д. 20',
                        info: '7. Переполнены мусорные баки',
                        status: 'В работе',
                        resident: 'Житель 7'
                    },
                    {
                        id: 8,
                        date: '23.04.2024 12:50',
                        adress: 'Ул. Окская, д. 20',
                        info: '8. Переполнены мусорные баки',
                        status: 'В работе',
                        resident: 'Житель 8'
                    },
                ]
            )
        },
        async loadRequestTasks({state, commit}, requestId) {
            // console.log(requestId)
            commit(
                'setRequestTasks',
                [
                    {employee: 'Сотрудник 1', task: 'Услуга 1', status: 'Новая'},
                    {employee: 'Сотрудник 2', task: 'Услуга 2', status: 'В работе'},
                    {employee: 'Сотрудник 3', task: 'Услуга 3', status: 'Новая'},
                    {employee: 'Сотрудник 4', task: 'Услуга 4', status: 'В работе'},
                    {employee: 'Сотрудник 5', task: 'Услуга 5', status: 'В работе'},
                    {employee: 'Сотрудник 6', task: 'Услуга 6', status: 'Новая'},
                ]
            )
        },
        async loadRequestData({state, commit}, requestId) {
            // console.log(requestId)
            commit(
                'setRequestData',
                {
                    id: 1,
                    date: '23.04.2024 16:00',
                    adress: 'Ул. Пупина, д. 13',
                    info: '1. Нет света',
                    status: 'Новая',
                    resident: 'Житель 1'
                }
            )
        }
    },
    namespaced: true
}