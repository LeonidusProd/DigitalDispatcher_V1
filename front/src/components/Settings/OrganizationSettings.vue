<template>
  <div class="inside-container">
    <div class="left-side">
      <div class="office-block">
        <div>
          <h3>Управляющие компании</h3>

          <OfficesList :key="this.officesListKey"
                       @deleteOffice="loadOffices"
                       :offices-list="this.officesList">

          </OfficesList>
        </div>

        <my-button @click="this.showOfficeDialog = true">
          Добавить УК
        </my-button>

        <create-office-popup :show="this.showOfficeDialog"
                             @saveOffice="saveOffice"
                             @closeOfficeDialog="this.showOfficeDialog = false">
        </create-office-popup>
      </div>
    </div>

    <div class="right-side">
      <div class="schedule-block">
        <div>
          <h3>Графики работы</h3>

          <WorkScheduleList :key="this.scheduleListKey"
                       @deleteSchedule="loadSchedules"
                       :schedules-list="this.schedulesList">

          </WorkScheduleList>
        </div>

        <my-button @click="this.showScheduleDialog = true">
          Добавить график работы
        </my-button>

        <WorkSchedulePopup :show="this.showScheduleDialog"
                             @saveSchedule="saveSchedule"
                             @closeScheduleDialog="this.showScheduleDialog = false">
        </WorkSchedulePopup>
      </div>

    </div>
  </div>
</template>

<script>
import MyInput from "@/components/UI/MyInput.vue";
import MyButton from "@/components/UI/MyButton.vue";
import CreateOfficePopup from "@/components/Settings/CreateOfficePopup.vue";
import axios from "axios";
import WorkScheduleList from "@/components/Settings/WorkScheduleList.vue";
import WorkSchedulePopup from "@/components/Settings/WorkSchedulePopup.vue";
import OfficesList from "@/components/Settings/OfficesList.vue";

export default {
  components: {OfficesList, WorkSchedulePopup, WorkScheduleList, CreateOfficePopup, MyButton, MyInput},
  data() {
    return {
      officesList: [],
      officesListKey: 1,
      showOfficeDialog: false,

      schedulesList: [],
      scheduleListKey: 1,
      showScheduleDialog: false,
    }
  },
  created() {
    this.loadOffices();
    this.loadSchedules()
  },
  methods: {
    async loadOffices() {
      const response = (await axios.get(`http://localhost:8000/api/v1/office/`))
      this.officesList = response.data
    },
    async createOffice(data) {
      try {
        await axios.post(
            'http://localhost:8000/api/v1/office/create/',
            {
              name: data.name,
              address: data.address,
              work_schedule: data.work_schedule
            }
        )
      } catch (e) {
        alert('Сервер не доступен')
      }
      this.reloadOffices()
    },
    saveOffice(data) {
      this.createOffice(data)
      this.showOfficeDialog = false
    },
    reloadOffices() {
      this.loadOffices();
      this.officesListKey = this.officesListKey + 1
    },

    async loadSchedules() {
      const response = (await axios.get(`http://localhost:8000/api/v1/schedule/`))
      this.schedulesList = response.data
      console.log(this.schedulesList)
    },
    async createSchedule(data) {
      try {
        const response = (await axios.post(
            'http://localhost:8000/api/v1/schedule/create/',
            {
              name: data.scheduleName,
            }
        ))
        let newSchedulePk = response.data.id
        console.log(response)
        await this.configWorkDays(newSchedulePk, data.days)
      } catch (e) {
        alert('Сервер не доступен')
      }
      // this.reloadSchedules()
    },
    async configWorkDays(newSchedulePk, days) {
      try {



        // const response = (await axios.post(
        //     'http://localhost:8000/api/v1/schedule/create/',
        //     {
        //       name: data.scheduleName,
        //     }
        // ))
      } catch (e) {
        alert('Сервер не доступен')
      }
      // this.reloadSchedules()
    },
    saveSchedule(data) {
      console.log(data)
      this.createSchedule(data)
      this.showScheduleDialog = false
    },
    reloadSchedules() {
      this.loadSchedules();
      this.scheduleListKey = this.scheduleListKey + 1
    },
  },
}

</script>

<style scoped>
.inside-container {
  display: flex;
  flex-direction: row;
  //justify-content: space-between;
  //border: 1px solid black;
  height: 100%;
  width: 100%;
}

.left-side {
  width: 35%;
  display: flex;
  flex-direction: column;
  justify-content: start;
  margin-right: 20px;
  //border: 1px solid blue;
}

.right-side {
  //width: 63%;
  width: 35%;
  display: flex;
  flex-direction: column;
  //justify-content: end;
  //align-items: end;
  //border: 1px solid red;
}

.office-block {
  height: 40%;
  //border: 1px solid green;
  justify-content: space-between;
  display: flex;
  flex-direction: column;
}

.schedule-block {
  height: 40%;
  //border: 1px solid green;
  justify-content: space-between;
  display: flex;
  flex-direction: column;
}

.save-button {
  width: 200px;
}
</style>