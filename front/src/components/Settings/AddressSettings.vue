<template>
  <div class="inside-container">
    <div class="outer-block left">
      <div class="inner-block">
        <div>
          <h3>Адреса</h3>

          <SettingsListView :key="this.addressesListKey"
                            :empty-header="'Список адресов пуст'"
                            :elements-list="this.addressesList"
                            :model-name="'address'"
                            @deleteElement="loadAddresses">
          </SettingsListView>
        </div>

        <MyButton @click="this.showAddressDialog = true">
          Добавить адрес
        </MyButton>

        <CreateAddressPopup :show="this.showAddressDialog"
                            @save="saveAddress"
                            @closeDialog="this.showAddressDialog = false">
        </CreateAddressPopup>
      </div>

      <div class="inner-block">
        <div>
          <h3>Жилой дом</h3>

          <SettingsListView :key="this.housesListKey"
                            :empty-header="'Список жилых домов пуст'"
                            :elements-list="this.housesList"
                            :model-name="'house'"
                            @deleteElement="loadHouses">
          </SettingsListView>
        </div>

        <MyButton @click="this.showHouseDialog = true">
          Добавить жилой дом
        </MyButton>

        <CreateHousePopup :show="this.showHouseDialog"
                          @save="saveHouse"
                          @closeDialog="this.showHouseDialog = false">
        </CreateHousePopup>
      </div>
    </div>

    <div class="outer-block">
      <div class="inner-block">
        <div>
          <h3>Жилой комплекс</h3>

          <SettingsListView :key="this.complexesListKey"
                            :empty-header="'Список жилых комплексов пуст'"
                            :elements-list="this.complexesList"
                            :model-name="'complex'"
                            @deleteElement="loadComplexes">
          </SettingsListView>
        </div>

        <MyButton @click="this.showComplexDialog = true">
          Добавить жилой комплекс
        </MyButton>

        <CreateComplexPopup :show="this.showComplexDialog"
                            @save="saveComplex"
                            @closeDialog="this.showComplexDialog = false">
        </CreateComplexPopup>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MyInput from "@/components/UI/MyInput.vue";
import MyButton from "@/components/UI/MyButton.vue";
import SettingsListView from "@/components/Settings/SettingsListView.vue";
import CreateComplexPopup from "@/components/Settings/CreateComplexPopup.vue";
import CreateAddressPopup from "@/components/Settings/CreateAddressPopup.vue";
import CreateHousePopup from "@/components/Settings/CreateHousePopup.vue";


export default {
  components: {
    CreateAddressPopup,
    CreateComplexPopup,
    CreateHousePopup,
    SettingsListView,
    MyButton,
    MyInput
  },
  data() {
    return {
      addressesList: [],
      addressesListKey: 1,
      showAddressDialog: false,

      complexesList: [],
      complexesListKey: 1,
      showComplexDialog: false,

      housesList: [],
      housesListKey: 1,
      showHouseDialog: false,
    }
  },
  created() {
    this.loadAddresses();
    this.loadComplexes();
    this.loadHouses();
  },
  methods: {
    async loadAddresses() {
      const response = (await axios.get(`http://localhost:8000/api/v1/address/`))
      this.addressesList = response.data
    },
    saveAddress() {
      this.loadAddresses();
      this.addressesListKey += 1
      this.showAddressDialog = false
    },

    async loadComplexes() {
      const response = (await axios.get(`http://localhost:8000/api/v1/complex/`))
      this.complexesList = response.data
    },
    saveComplex() {
      this.loadComplexes();
      this.complexesListKey += 1
      this.showComplexDialog = false
    },

    async loadHouses() {
      const response = (await axios.get(`http://localhost:8000/api/v1/house/`))
      this.housesList = response.data
    },
    saveHouse() {
      this.loadHouses();
      this.housesListKey += 1
      this.showHouseDialog = false
    },
  },
}

</script>

<style scoped>
.inside-container {
  display: flex;
  flex-direction: row;
  height: 100%;
  width: 100%;
}

.outer-block {
  width: 35%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-right: 20px;
}

.inner-block {
  height: 45%;
  justify-content: space-between;
  display: flex;
  flex-direction: column;
}

.left {
  width: 55%;
}
</style>