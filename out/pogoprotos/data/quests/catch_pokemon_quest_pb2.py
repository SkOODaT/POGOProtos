# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/quests/catch_pokemon_quest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/quests/catch_pokemon_quest.proto',
  package='pogoprotos.data.quests',
  syntax='proto3',
  serialized_pb=_b('\n0pogoprotos/data/quests/catch_pokemon_quest.proto\x12\x16pogoprotos.data.quests\"\x13\n\x11\x43\x61tchPokemonQuestb\x06proto3')
)




_CATCHPOKEMONQUEST = _descriptor.Descriptor(
  name='CatchPokemonQuest',
  full_name='pogoprotos.data.quests.CatchPokemonQuest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=95,
)

DESCRIPTOR.message_types_by_name['CatchPokemonQuest'] = _CATCHPOKEMONQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CatchPokemonQuest = _reflection.GeneratedProtocolMessageType('CatchPokemonQuest', (_message.Message,), dict(
  DESCRIPTOR = _CATCHPOKEMONQUEST,
  __module__ = 'pogoprotos.data.quests.catch_pokemon_quest_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.CatchPokemonQuest)
  ))
_sym_db.RegisterMessage(CatchPokemonQuest)


# @@protoc_insertion_point(module_scope)
