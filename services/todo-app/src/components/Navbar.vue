<template>
  
  <nav>
  <v-app-bar app color="#B399D4" dark elevation="0">

    <v-app-bar-nav-icon color="black" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    <v-toolbar-title class="white--text">
      <span class="font-weight-light"> ToDo </span>
      <span> Challenge </span>
    </v-toolbar-title>
    <v-spacer></v-spacer>

    
  </v-app-bar>

  <v-navigation-drawer
      v-model="drawer"
      absolute
      bottom
      temporary
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group 
          v-model="group"
          active-class="deep-grey--text text--accent-4"  
        >
          <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
            <v-list-item-title>{{link.text}}</v-list-item-title>
          </v-list-item>
          
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>

<script>
  export default {
    data: () => ({
      drawer: false,
      links: [
        { text: 'Home', route: '/' },
        { text: 'Tarefas' , route: '/tasks'}
      ],
      group: null,
    }),

    watch: {
      group () {
        this.drawer = false
      },
    },
  }
</script>