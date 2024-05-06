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
                             @closeDialog="this.showOfficeDialog = false"
                             @saveOffice="saveOffice">
        </create-office-popup>
      </div>

    </div>

    <div class="right-side">

    </div>
  </div>
</template>

<script>
import MyInput from "@/components/UI/MyInput.vue";
import MyButton from "@/components/UI/MyButton.vue";
import OfficesList from "@/components/Settings/OfficesList.vue";
import CreateOfficePopup from "@/components/Settings/CreateOfficePopup.vue";
import axios from "axios";

export default {
  components: {CreateOfficePopup, MyButton, OfficesList, MyInput},
  data() {
    return {
      officesList: [],
      officesListKey: 1,
      showOfficeDialog: false,
    }
  },
  mounted() {
    this.loadOffices()
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
    },
    saveOffice(data) {
      this.createOffice(data)
      this.reloadOffices()
    },
    reloadOffices() {
      this.loadOffices();
      this.officesListKey += 1

    },
  },
}

</script>

<style scoped>
.inside-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  border: 1px solid black;
  height: 100%;
  width: 100%;
}

.left-side {
  width: 35%;
  display: flex;
  flex-direction: column;
  justify-content: start;
  border: 1px solid blue;
}

.right-side {
  width: 63%;
  display: flex;
  flex-direction: column;
  justify-content: end;
  align-items: end;
  border: 1px solid red;
}

.office-block {
  height: 40%;
  border: 1px solid green;
  justify-content: space-between;
  display: flex;
  flex-direction: column;
}

.save-button {
  width: 200px;
}
</style>