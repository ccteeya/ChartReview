<template>
	<Header></Header>
	
	<v-container>
		<v-row justify="end" no-gutters>
			<!-- <v-col> -->
				<v-btn color="success">succ</v-btn>
				<v-btn color="success">succ</v-btn>
				<!-- <v-spacer></v-spacer> -->
			<!-- </v-col> -->
			<!-- <v-col> -->
				<v-btn color="success">succ</v-btn>
				<v-btn color="success">succ</v-btn>
			<!-- </v-col> -->
		</v-row>
		 
		<v-row justify="start" no-gutters>
			<v-col cols="2"><v-btn color="success">succ</v-btn></v-col>
			<v-col cols="4"><v-btn color="success">succ</v-btn></v-col>
			<v-col cols="6"><v-btn color="success">succ</v-btn></v-col>
			
		</v-row>
	</v-container>
</template>

<script>
// import HelloWorld from '../components/HelloWorld.vue';
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
export default {
  name: 'Home',
  
  components: {
    // HelloWorld,
	Footer,
	Header,
  },
};
</script>
