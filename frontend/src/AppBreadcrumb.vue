<template>
	<div class="layout-breadcrumb-container">
		<div class="layout-breadcrumb-left-items">
			<a href="#" class="menu-button" @click="onMenuButtonClick($event)" v-if="isStatic()">
				<i class="pi pi-bars"></i>
			</a>

			<Breadcrumb :model="items" class="layout-breadcrumb"></Breadcrumb>
		</div>
		<div class="layout-breadcrumb-right-items">
			<a tabindex="0" class="search-icon" @click="breadcrumbClick">
				<i class="pi pi-search"></i>
			</a>

			<div class="search-wrapper" :class="{'active-search-wrapper': searchActive}">
				<span class="p-input-icon-left">
					<i class="pi pi-search"></i>
					<InputText placeholder="Search..." v-model="search" @click="inputClick"/>
				</span>
			</div>

			<span class="layout-rightmenu-button-desktop">
				<Button label="Today" icon="pi pi-bookmark"
					class="layout-rightmenu-button" @click="onRightMenuButtonClick()"></Button>
			</span>
			
			<span class="layout-rightmenu-button-mobile">
				<Button icon="pi pi-bookmark"
					class="layout-rightmenu-button" @click="onRightMenuButtonClick()"></Button>
			</span>
		</div>
	</div>
</template>

<script>
export default {
	props: {
		menuMode: String,
		searchActive: {
			type: Boolean,
			default: false
		},
		searchClick: {
			type: Boolean,
			default: false
		}
	},
	emits: ['menubutton-click', 'rightmenu-button-click', 'update:searchActive', 'update:searchClick'],
	data() {
		return {
			items: [],
			search: ''
		}
	},
	watch: {
		$route() {
			this.watchRouter();
		}
	},
	created() {
		this.watchRouter();
	},
	methods: {
		watchRouter() {
			if(this.$router.currentRoute.value.meta.breadcrumb) {
				this.items = [];
				const bc = this.$router.currentRoute.value.meta.breadcrumb[0];
				for(let pro in bc) {
					this.items.push({label: bc[pro]});
				}
			}
		},
		onMenuButtonClick(event) {
			this.$emit('menubutton-click', event);
		},
		onRightMenuButtonClick() {
			this.$emit('rightmenu-button-click');
		},
		inputClick() {
			this.$emit('update:searchClick', true);
		},
		breadcrumbClick() {
			this.$emit('update:searchActive', true);
			this.$emit('update:searchClick', true);
		},
		isStatic() {
			return this.menuMode === 'static';
		}
	}
}
</script>

<style scoped>
::v-deep(.p-breadcrumb > ul > li.p-breadcrumb-chevron:first-of-type) { 
	display: none;
}
</style>