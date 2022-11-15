# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bond.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nbond.proto\x12\x0b\x62ondPackage\"\"\n\x0bLoadRequest\x12\x13\n\x0b\x62itfileName\x18\x01 \x01(\t\"0\n\x0cLoadResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1e\n\x0cInputRequest\x12\x0e\n\x06inputs\x18\x01 \x01(\t\" \n\rInputResponse\x12\x0f\n\x07outputs\x18\x01 \x01(\t2\x8d\x01\n\nBondServer\x12=\n\x04load\x12\x18.bondPackage.LoadRequest\x1a\x19.bondPackage.LoadResponse\"\x00\x12@\n\x07predict\x12\x18.bondPackage.LoadRequest\x1a\x19.bondPackage.LoadResponse\"\x00\x62\x06proto3')



_LOADREQUEST = DESCRIPTOR.message_types_by_name['LoadRequest']
_LOADRESPONSE = DESCRIPTOR.message_types_by_name['LoadResponse']
_INPUTREQUEST = DESCRIPTOR.message_types_by_name['InputRequest']
_INPUTRESPONSE = DESCRIPTOR.message_types_by_name['InputResponse']
LoadRequest = _reflection.GeneratedProtocolMessageType('LoadRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOADREQUEST,
  '__module__' : 'bond_pb2'
  # @@protoc_insertion_point(class_scope:bondPackage.LoadRequest)
  })
_sym_db.RegisterMessage(LoadRequest)

LoadResponse = _reflection.GeneratedProtocolMessageType('LoadResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOADRESPONSE,
  '__module__' : 'bond_pb2'
  # @@protoc_insertion_point(class_scope:bondPackage.LoadResponse)
  })
_sym_db.RegisterMessage(LoadResponse)

InputRequest = _reflection.GeneratedProtocolMessageType('InputRequest', (_message.Message,), {
  'DESCRIPTOR' : _INPUTREQUEST,
  '__module__' : 'bond_pb2'
  # @@protoc_insertion_point(class_scope:bondPackage.InputRequest)
  })
_sym_db.RegisterMessage(InputRequest)

InputResponse = _reflection.GeneratedProtocolMessageType('InputResponse', (_message.Message,), {
  'DESCRIPTOR' : _INPUTRESPONSE,
  '__module__' : 'bond_pb2'
  # @@protoc_insertion_point(class_scope:bondPackage.InputResponse)
  })
_sym_db.RegisterMessage(InputResponse)

_BONDSERVER = DESCRIPTOR.services_by_name['BondServer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOADREQUEST._serialized_start=27
  _LOADREQUEST._serialized_end=61
  _LOADRESPONSE._serialized_start=63
  _LOADRESPONSE._serialized_end=111
  _INPUTREQUEST._serialized_start=113
  _INPUTREQUEST._serialized_end=143
  _INPUTRESPONSE._serialized_start=145
  _INPUTRESPONSE._serialized_end=177
  _BONDSERVER._serialized_start=180
  _BONDSERVER._serialized_end=321
# @@protoc_insertion_point(module_scope)
