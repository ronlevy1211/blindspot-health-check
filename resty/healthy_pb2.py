# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: healthy.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rhealthy.proto\"#\n\x0fSecurityRequest\x12\x10\n\x08packages\x18\x01 \x03(\t\"1\n\x10SecurityResponse\x12\x1d\n\x15security_check_result\x18\x01 \x03(\t2J\n\x12HealthCheckService\x12\x34\n\rCheckSecurity\x12\x10.SecurityRequest\x1a\x11.SecurityResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'healthy_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SECURITYREQUEST._serialized_start=17
  _SECURITYREQUEST._serialized_end=52
  _SECURITYRESPONSE._serialized_start=54
  _SECURITYRESPONSE._serialized_end=103
  _HEALTHCHECKSERVICE._serialized_start=105
  _HEALTHCHECKSERVICE._serialized_end=179
# @@protoc_insertion_point(module_scope)
