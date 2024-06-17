<template>
  <tasks-page/>
</template>

<script lang="ts">
  import Vue from 'vue'
  import TasksPage from '../components/TasksPage.vue'

  export default Vue.extend({
    name: 'Tasks',

    components: {
      TasksPage,
    },
  })
</script>
