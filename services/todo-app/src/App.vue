<template>
  <v-app id="app">
    <navbar />

    <v-main>
      <router-view/>
    </v-main>


  </v-app>
</template>

<style>
#app{
  background-color: #F5E1FD;
}
</style>

<script lang="ts">
import Navbar from './components/Navbar.vue'
import Vue from 'vue';

export default Vue.extend({
  name: 'App',
  components: {Navbar},
  data: () => ({
    //
  }),
});
</script>
