# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/avatar_customization_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.player import player_avatar_type_pb2 as pogoprotos_dot_data_dot_player_dot_player__avatar__type__pb2
from pogoprotos.enums import badge_type_pb2 as pogoprotos_dot_enums_dot_badge__type__pb2
from pogoprotos.data.avatar import avatar_customization_pb2 as pogoprotos_dot_data_dot_avatar_dot_avatar__customization__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/avatar_customization_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_pb=_b('\n>pogoprotos/settings/master/avatar_customization_settings.proto\x12\x1apogoprotos.settings.master\x1a/pogoprotos/data/player/player_avatar_type.proto\x1a!pogoprotos/enums/badge_type.proto\x1a\x31pogoprotos/data/avatar/avatar_customization.proto\"\xb2\x06\n\x1b\x41vatarCustomizationSettings\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12=\n\x0b\x61vatar_type\x18\x02 \x01(\x0e\x32(.pogoprotos.data.player.PlayerAvatarType\x12>\n\x04slot\x18\x03 \x03(\x0e\x32\x30.pogoprotos.data.avatar.AvatarCustomization.Slot\x12\x13\n\x0b\x62undle_name\x18\x04 \x01(\t\x12\x12\n\nasset_name\x18\x05 \x01(\t\x12\x12\n\ngroup_name\x18\x06 \x01(\t\x12\x12\n\nsort_order\x18\x07 \x01(\x05\x12j\n\x0bunlock_type\x18\x08 \x01(\x0e\x32U.pogoprotos.settings.master.AvatarCustomizationSettings.AvatarCustomizationUnlockType\x12h\n\npromo_type\x18\t \x03(\x0e\x32T.pogoprotos.settings.master.AvatarCustomizationSettings.AvatarCustomizationPromoType\x12\x36\n\x11unlock_badge_type\x18\n \x01(\x0e\x32\x1b.pogoprotos.enums.BadgeType\x12\x0f\n\x07iap_sku\x18\x0b \x01(\t\x12\x1a\n\x12unlock_badge_level\x18\x0c \x01(\x05\x12\x11\n\ticon_name\x18\r \x01(\t\x12\x1b\n\x13unlock_player_level\x18\x0e \x01(\x05\"L\n\x1c\x41vatarCustomizationPromoType\x12\x14\n\x10UNSET_PROMO_TYPE\x10\x00\x12\x08\n\x04SALE\x10\x01\x12\x0c\n\x08\x46\x45\x41TURED\x10\x02\"y\n\x1d\x41vatarCustomizationUnlockType\x12\x15\n\x11UNSET_UNLOCK_TYPE\x10\x00\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x01\x12\x10\n\x0cMEDAL_REWARD\x10\x02\x12\x10\n\x0cIAP_CLOTHING\x10\x03\x12\x10\n\x0cLEVEL_REWARD\x10\x04\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_player_dot_player__avatar__type__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_badge__type__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_avatar_dot_avatar__customization__pb2.DESCRIPTOR,])



_AVATARCUSTOMIZATIONSETTINGS_AVATARCUSTOMIZATIONPROMOTYPE = _descriptor.EnumDescriptor(
  name='AvatarCustomizationPromoType',
  full_name='pogoprotos.settings.master.AvatarCustomizationSettings.AvatarCustomizationPromoType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_PROMO_TYPE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SALE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEATURED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=849,
  serialized_end=925,
)
_sym_db.RegisterEnumDescriptor(_AVATARCUSTOMIZATIONSETTINGS_AVATARCUSTOMIZATIONPROMOTYPE)

_AVATARCUSTOMIZATIONSETTINGS_AVATARCUSTOMIZATIONUNLOCKTYPE = _descriptor.EnumDescriptor(
  name='AvatarCustomizationUnlockType',
  full_name='pogoprotos.settings.master.AvatarCustomizationSettings.AvatarCustomizationUnlockType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_UNLOCK_TYPE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDAL_REWARD', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAP_CLOTHING', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEVEL_REWARD', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=927,
  serialized_end=1048,
)
_sym_db.RegisterEnumDescriptor(_AVATARCUSTOMIZATIONSETTINGS_AVATARCUSTOMIZATIONUNLOCKTYPE)


_AVATARCUSTOMIZATIONSETTINGS = _descriptor.Descriptor(
  name='AvatarCustomizationSettings',
  full_name='pogoprotos.settings.master.AvatarCustomizationSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='pogoprotos.settings.master.AvatarCustomizationSettings.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_type', full_name='pogoprotos.settings.master.AvatarCustomizationSettings.avatar_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot', full_name='pogoprotos.settings.master.AvatarCustomizationSettings.slot', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bundle_name', full_name='pogoprotos.settings.master.AvatarCustomizationSettings.bundle_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='asset_name', full_name='pogoprotos.settings.master.AvatarCustomizationSettings.asset_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_name', full_name='pogoprotos.settings.master.AvatarCustomizationSettings.group_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_order', full_name='pogoprotos.settings.master.AvatarCustomizationSettings.sort_order', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unlock_type', full_name='pogoprotos.settings.master.AvatarCustomizationSettings.unlock_type', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='promo_type', full_name='pogoprotos.settings.master.AvatarCustomizationSettings.promo_type', index=8,
      number=9, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unlock_badge_type', full_name='pogoprotos.settings.master.AvatarCustomizationSettings.unlock_badge_type', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iap_sku', full_name='pogoprotos.settings.master.AvatarCustomizationSettings.iap_sku', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unlock_badge_level', full_name='pogoprotos.settings.master.AvatarCustomizationSettings.unlock_badge_level', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='icon_name', full_name='pogoprotos.settings.master.AvatarCustomizationSettings.icon_name', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unlock_player_level', full_name='pogoprotos.settings.master.AvatarCustomizationSettings.unlock_player_level', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AVATARCUSTOMIZATIONSETTINGS_AVATARCUSTOMIZATIONPROMOTYPE,
    _AVATARCUSTOMIZATIONSETTINGS_AVATARCUSTOMIZATIONUNLOCKTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=1048,
)

_AVATARCUSTOMIZATIONSETTINGS.fields_by_name['avatar_type'].enum_type = pogoprotos_dot_data_dot_player_dot_player__avatar__type__pb2._PLAYERAVATARTYPE
_AVATARCUSTOMIZATIONSETTINGS.fields_by_name['slot'].enum_type = pogoprotos_dot_data_dot_avatar_dot_avatar__customization__pb2._AVATARCUSTOMIZATION_SLOT
_AVATARCUSTOMIZATIONSETTINGS.fields_by_name['unlock_type'].enum_type = _AVATARCUSTOMIZATIONSETTINGS_AVATARCUSTOMIZATIONUNLOCKTYPE
_AVATARCUSTOMIZATIONSETTINGS.fields_by_name['promo_type'].enum_type = _AVATARCUSTOMIZATIONSETTINGS_AVATARCUSTOMIZATIONPROMOTYPE
_AVATARCUSTOMIZATIONSETTINGS.fields_by_name['unlock_badge_type'].enum_type = pogoprotos_dot_enums_dot_badge__type__pb2._BADGETYPE
_AVATARCUSTOMIZATIONSETTINGS_AVATARCUSTOMIZATIONPROMOTYPE.containing_type = _AVATARCUSTOMIZATIONSETTINGS
_AVATARCUSTOMIZATIONSETTINGS_AVATARCUSTOMIZATIONUNLOCKTYPE.containing_type = _AVATARCUSTOMIZATIONSETTINGS
DESCRIPTOR.message_types_by_name['AvatarCustomizationSettings'] = _AVATARCUSTOMIZATIONSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AvatarCustomizationSettings = _reflection.GeneratedProtocolMessageType('AvatarCustomizationSettings', (_message.Message,), dict(
  DESCRIPTOR = _AVATARCUSTOMIZATIONSETTINGS,
  __module__ = 'pogoprotos.settings.master.avatar_customization_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.AvatarCustomizationSettings)
  ))
_sym_db.RegisterMessage(AvatarCustomizationSettings)


# @@protoc_insertion_point(module_scope)
