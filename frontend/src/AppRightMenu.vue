<template>
	<div class="layout-rightmenu" :class="{'layout-rightmenu-active': rightMenuActive}" @click="onRightMenuClick($event)">
		<a href="#" @click="onChangeRightMenuActive" class="layout-rightmenu-close">
			<i class="pi pi-times"></i>
		</a>
		<div class="user-detail-wrapper">
			<div class="user-detail-content">
				<img src="layout/images/dashboard/gene.png" alt="atlantis" class="user-image">
				<span class="user-name">Gene Russell</span>
				<span class="user-number">(406) 555-0120</span>
			</div>
			<div class="user-tasks">
				<div class="user-tasks-item in-progress">
					<a class="task-number">23</a>
					<span class="task-name">Progress</span>
				</div>
				<div class="user-tasks-item">
					<a class="task-number">6</a>
					<span class="task-name">Overdue</span>
				</div>
				<div class="user-tasks-item">
					<a class="task-number">38</a>
					<span class="task-name">All deals</span>
				</div>
			</div>
		</div>
		<div>
			<Calendar v-model="date" :inline="true"></Calendar>
		</div>
		<div class="daily-plan-wrapper">
			<span class="today-date">14 Sunday, Jun 2020</span>
			<ul>
				<li>
					<span class="event-time">1:00 PM - 2:00 PM</span>
					<span class="event-topic">Meeting with Alfredo Rhiel Madsen</span>
				</li>
				<li>
					<span class="event-time">2:00 PM - 3:00 PM</span>
					<span class="event-topic">Team Sync</span>
				</li>
				<li>
					<span class="event-time">5:00 PM - 6:00 PM</span>
					<span class="event-topic">Team Sync</span>
				</li>
				<li>
					<span class="event-time">7:00 PM - 7:30 PM</span>
					<span class="event-topic">Meeting with Engineering managers</span>
				</li>
			</ul>
		</div>
	</div>
</template>

<script>
export default {
	props: {
		rightMenuActive: {
			type: Boolean,
			default: false
		}
	},
	emits: ['rightmenu-active', 'rightmenu-click'],
	data() {
		return {
			date: null
		}
	},
	methods: {
		onChangeRightMenuActive() {
			this.$emit('rightmenu-active', false);
		},
		onRightMenuClick() {
			this.$emit('rightmenu-click');
		}
	}
}
</script>