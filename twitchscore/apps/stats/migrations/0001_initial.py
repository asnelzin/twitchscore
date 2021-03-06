# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table(u'stats_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.User'])),
            ('champion_id', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('game_mode', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('game_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('invalid', self.gf('django.db.models.fields.BooleanField')()),
            ('ip_earned', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('level', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('map_id', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('spell1', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('spell2', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('sub_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('team_id', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'stats', ['Game'])

        # Adding model 'Player'
        db.create_table(u'stats_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('champion_id', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('summoner_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('team_id', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.Game'])),
        ))
        db.send_create_signal(u'stats', ['Player'])

        # Adding model 'Stats'
        db.create_table(u'stats_stats', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('assists', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('barracks_killed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('champions_killed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('combat_player_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('consumables_purchased', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('damage_dealt_player', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('double_kills', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('first_blood', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gold', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gold_earned', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gold_spent', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item0', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item3', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item4', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item5', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item6', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('items_purchased', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('killing_sprees', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('largest_critical_strike', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('largest_killing_spree', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('largest_multi_kill', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('legendary_items_created', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('magic_damage_dealt_player', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('magic_damage_dealt_to_champions', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('magic_damage_taken', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('minions_denied', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('minions_killed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('neutral_minions_killed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('neutral_minions_killed_enemy_jungle', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('neutral_minions_killed_your_jungle', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nexus_killed', self.gf('django.db.models.fields.BooleanField')()),
            ('node_capture', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('node_capture_assist', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('node_neutralize', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('node_neutralize_assist', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('num_deaths', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('num_items_bought', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('objective_player_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('penta_kills', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('physical_damage_dealt_player', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('physical_damage_dealt_to_champions', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('physical_damage_taken', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('quadra_kills', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sight_wards_bought', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('spell1_cast', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('spell2_cast', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('spell3_cast', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('spell4_cast', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('summon_spell1_cast', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('summon_spell2_cast', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('super_monster_killed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('team', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('team_objective', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('time_played', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total_damage_dealt', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total_damage_dealt_to_champions', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total_damage_taken', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total_heal', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total_player_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total_score_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total_time_crowd_control_dealt', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total_units_healed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('triple_kills', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('true_damage_dealt_player', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('true_damage_dealt_to_champions', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('true_damage_taken', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('turrets_killed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('unreal_kills', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('victory_point_total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('vision_wards_bought', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ward_killed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ward_placed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('win', self.gf('django.db.models.fields.BooleanField')()),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.Game'], blank=True)),
        ))
        db.send_create_signal(u'stats', ['Stats'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table(u'stats_game')

        # Deleting model 'Player'
        db.delete_table(u'stats_player')

        # Deleting model 'Stats'
        db.delete_table(u'stats_stats')


    models = {
        u'accounts.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'summoner_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'summoner_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'stats.game': {
            'Meta': {'object_name': 'Game'},
            'champion_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {}),
            'game_mode': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'game_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invalid': ('django.db.models.fields.BooleanField', [], {}),
            'ip_earned': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'map_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'spell1': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'spell2': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'sub_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'team_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.User']"})
        },
        u'stats.player': {
            'Meta': {'object_name': 'Player'},
            'champion_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'summoner_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'team_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'stats.stats': {
            'Meta': {'object_name': 'Stats'},
            'assists': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'barracks_killed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'champions_killed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'combat_player_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'consumables_purchased': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'damage_dealt_player': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'double_kills': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_blood': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.Game']", 'blank': 'True'}),
            'gold': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gold_earned': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gold_spent': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item0': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'item1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'item2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'item3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'item4': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'item5': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'item6': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'items_purchased': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'killing_sprees': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'largest_critical_strike': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'largest_killing_spree': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'largest_multi_kill': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'legendary_items_created': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'magic_damage_dealt_player': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'magic_damage_dealt_to_champions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'magic_damage_taken': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'minions_denied': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'minions_killed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'neutral_minions_killed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'neutral_minions_killed_enemy_jungle': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'neutral_minions_killed_your_jungle': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nexus_killed': ('django.db.models.fields.BooleanField', [], {}),
            'node_capture': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'node_capture_assist': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'node_neutralize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'node_neutralize_assist': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_deaths': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_items_bought': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'objective_player_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'penta_kills': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'physical_damage_dealt_player': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'physical_damage_dealt_to_champions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'physical_damage_taken': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quadra_kills': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sight_wards_bought': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'spell1_cast': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'spell2_cast': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'spell3_cast': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'spell4_cast': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'summon_spell1_cast': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'summon_spell2_cast': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'super_monster_killed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team_objective': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_played': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_damage_dealt': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_damage_dealt_to_champions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_damage_taken': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_heal': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_player_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_score_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_time_crowd_control_dealt': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_units_healed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'triple_kills': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'true_damage_dealt_player': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'true_damage_dealt_to_champions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'true_damage_taken': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'turrets_killed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'unreal_kills': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'victory_point_total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vision_wards_bought': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ward_killed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ward_placed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'win': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['stats']