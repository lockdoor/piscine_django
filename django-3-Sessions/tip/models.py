from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.http import HttpRequest
from django.contrib.auth.models import Permission

# Create your models here.

# Add reputation field to User
class CustomUser(AbstractUser):
    reputation = models.IntegerField(default=0)

class Tip(models.Model):
	content = models.TextField()
	author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	upvote = models.ManyToManyField(CustomUser, related_name='upvote')
	downvote = models.ManyToManyField(CustomUser, related_name='downvote')
	date = models.DateField(auto_now_add=True)

	class Meta:
		permissions = [
			('can_downvote_tip', 'Can downvote tip'),
		]
		ordering = ['-date']

	def __str__(self):
		return self.author.username

	# for default permission add, change, delete, view not prefix can_
	def set_premissoins(self):
		can_delete = Permission.objects.get(codename='delete_tip')
		can_downvote = Permission.objects.get(codename='can_downvote_tip')
		if self.author.reputation >= 30 and not self.author.has_perm(perm='tip.delete_tip'):
			self.author.user_permissions.add(can_delete)
		elif self.author.reputation >= 15 and self.author.reputation < 30:
			if self.author.has_perm(perm='tip.delete_tip'):
				self.author.user_permissions.remove(can_delete)
			if not self.author.has_perm(perm='tip.can_downvote_tip'):
				self.author.user_permissions.add(can_downvote)
		elif self.author.reputation < 15 and self.author.has_perm(perm='tip.can_downvote_tip'):
			self.author.user_permissions.remove(can_downvote)

	def set_upvote(self, request: HttpRequest):
		if self.downvote.filter(pk=request.user.pk).exists():
			self.downvote.remove(request.user)
			self.author.reputation += 2
		
		if self.upvote.filter(pk=request.user.pk).exists():
			self.upvote.remove(request.user)
			self.author.reputation -= 5
		else:
			self.upvote.add(request.user)
			self.author.reputation += 5

		self.author.save()
		
		self.set_premissoins()

		return True

	def set_downvote(self, request: HttpRequest):
		if self.author == request.user or request.user.has_perm(perm='tip.can_downvote_tip'):
			if self.upvote.filter(pk=request.user.pk).exists():
				self.upvote.remove(request.user)
				self.author.reputation -= 5
			if self.downvote.filter(pk=request.user.pk).exists():
				self.downvote.remove(request.user)
				self.author.reputation += 2
			else:
				self.downvote.add(request.user)
				self.author.reputation -= 2

			self.author.save()
			self.set_premissoins()
			
			return True
		else:
			return False
