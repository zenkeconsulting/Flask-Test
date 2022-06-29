<template>
	<div class="exception-body error">
		<div class="exception-panel">
			<h1>ERROR</h1>
			<h3>something's went
				wrong</h3>
			<router-link to="/">
				<Button type="button" label="Go back to home"></Button>
			</router-link>
		</div>
		<div class="exception-footer">
			<img :src="'layout/images/logo-'+ color + '.png'" class="exception-logo"/>
			<img :src="'layout/images/appname-'+ color + '.png'" class="exception-appname"/>
		</div>
	</div>
</template>

<script>
export default {
	computed: {
		color() {
			if (this.$appState.colorScheme === 'light') return 'dark';
			return 'light';
		}
	}
}
</script>

<style scoped>
</style>
