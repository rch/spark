#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spark/connect/base.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from pyspark.sql.connect.proto import commands_pb2 as spark_dot_connect_dot_commands__pb2
from pyspark.sql.connect.proto import relations_pb2 as spark_dot_connect_dot_relations__pb2
from pyspark.sql.connect.proto import types_pb2 as spark_dot_connect_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x18spark/connect/base.proto\x12\rspark.connect\x1a\x19google/protobuf/any.proto\x1a\x1cspark/connect/commands.proto\x1a\x1dspark/connect/relations.proto\x1a\x19spark/connect/types.proto"t\n\x04Plan\x12-\n\x04root\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationH\x00R\x04root\x12\x32\n\x07\x63ommand\x18\x02 \x01(\x0b\x32\x16.spark.connect.CommandH\x00R\x07\x63ommandB\t\n\x07op_type"\xb5\x01\n\x07\x45xplain\x12\x45\n\x0c\x65xplain_mode\x18\x01 \x01(\x0e\x32".spark.connect.Explain.ExplainModeR\x0b\x65xplainMode"c\n\x0b\x45xplainMode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\n\n\x06SIMPLE\x10\x01\x12\x0c\n\x08\x45XTENDED\x10\x02\x12\x0b\n\x07\x43ODEGEN\x10\x03\x12\x08\n\x04\x43OST\x10\x04\x12\r\n\tFORMATTED\x10\x05"z\n\x0bUserContext\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x1b\n\tuser_name\x18\x02 \x01(\tR\x08userName\x12\x35\n\nextensions\x18\xe7\x07 \x03(\x0b\x32\x14.google.protobuf.AnyR\nextensions"\x81\x02\n\x12\x41nalyzePlanRequest\x12\x1b\n\tclient_id\x18\x01 \x01(\tR\x08\x63lientId\x12=\n\x0cuser_context\x18\x02 \x01(\x0b\x32\x1a.spark.connect.UserContextR\x0buserContext\x12\'\n\x04plan\x18\x03 \x01(\x0b\x32\x13.spark.connect.PlanR\x04plan\x12$\n\x0b\x63lient_type\x18\x04 \x01(\tH\x00R\nclientType\x88\x01\x01\x12\x30\n\x07\x65xplain\x18\x05 \x01(\x0b\x32\x16.spark.connect.ExplainR\x07\x65xplainB\x0e\n\x0c_client_type"\x8a\x02\n\x13\x41nalyzePlanResponse\x12\x1b\n\tclient_id\x18\x01 \x01(\tR\x08\x63lientId\x12/\n\x06schema\x18\x02 \x01(\x0b\x32\x17.spark.connect.DataTypeR\x06schema\x12%\n\x0e\x65xplain_string\x18\x03 \x01(\tR\rexplainString\x12\x1f\n\x0btree_string\x18\x04 \x01(\tR\ntreeString\x12\x19\n\x08is_local\x18\x05 \x01(\x08R\x07isLocal\x12!\n\x0cis_streaming\x18\x06 \x01(\x08R\x0bisStreaming\x12\x1f\n\x0binput_files\x18\x07 \x03(\tR\ninputFiles"\xcf\x01\n\x12\x45xecutePlanRequest\x12\x1b\n\tclient_id\x18\x01 \x01(\tR\x08\x63lientId\x12=\n\x0cuser_context\x18\x02 \x01(\x0b\x32\x1a.spark.connect.UserContextR\x0buserContext\x12\'\n\x04plan\x18\x03 \x01(\x0b\x32\x13.spark.connect.PlanR\x04plan\x12$\n\x0b\x63lient_type\x18\x04 \x01(\tH\x00R\nclientType\x88\x01\x01\x42\x0e\n\x0c_client_type"\x8f\x06\n\x13\x45xecutePlanResponse\x12\x1b\n\tclient_id\x18\x01 \x01(\tR\x08\x63lientId\x12N\n\x0b\x61rrow_batch\x18\x02 \x01(\x0b\x32-.spark.connect.ExecutePlanResponse.ArrowBatchR\narrowBatch\x12\x44\n\x07metrics\x18\x04 \x01(\x0b\x32*.spark.connect.ExecutePlanResponse.MetricsR\x07metrics\x1a=\n\nArrowBatch\x12\x1b\n\trow_count\x18\x01 \x01(\x03R\x08rowCount\x12\x12\n\x04\x64\x61ta\x18\x02 \x01(\x0cR\x04\x64\x61ta\x1a\x85\x04\n\x07Metrics\x12Q\n\x07metrics\x18\x01 \x03(\x0b\x32\x37.spark.connect.ExecutePlanResponse.Metrics.MetricObjectR\x07metrics\x1a\xcc\x02\n\x0cMetricObject\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x17\n\x07plan_id\x18\x02 \x01(\x03R\x06planId\x12\x16\n\x06parent\x18\x03 \x01(\x03R\x06parent\x12z\n\x11\x65xecution_metrics\x18\x04 \x03(\x0b\x32M.spark.connect.ExecutePlanResponse.Metrics.MetricObject.ExecutionMetricsEntryR\x10\x65xecutionMetrics\x1a{\n\x15\x45xecutionMetricsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12L\n\x05value\x18\x02 \x01(\x0b\x32\x36.spark.connect.ExecutePlanResponse.Metrics.MetricValueR\x05value:\x02\x38\x01\x1aX\n\x0bMetricValue\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05value\x18\x02 \x01(\x03R\x05value\x12\x1f\n\x0bmetric_type\x18\x03 \x01(\tR\nmetricType2\xc7\x01\n\x13SparkConnectService\x12X\n\x0b\x45xecutePlan\x12!.spark.connect.ExecutePlanRequest\x1a".spark.connect.ExecutePlanResponse"\x00\x30\x01\x12V\n\x0b\x41nalyzePlan\x12!.spark.connect.AnalyzePlanRequest\x1a".spark.connect.AnalyzePlanResponse"\x00\x42"\n\x1eorg.apache.spark.connect.protoP\x01\x62\x06proto3'
)


_PLAN = DESCRIPTOR.message_types_by_name["Plan"]
_EXPLAIN = DESCRIPTOR.message_types_by_name["Explain"]
_USERCONTEXT = DESCRIPTOR.message_types_by_name["UserContext"]
_ANALYZEPLANREQUEST = DESCRIPTOR.message_types_by_name["AnalyzePlanRequest"]
_ANALYZEPLANRESPONSE = DESCRIPTOR.message_types_by_name["AnalyzePlanResponse"]
_EXECUTEPLANREQUEST = DESCRIPTOR.message_types_by_name["ExecutePlanRequest"]
_EXECUTEPLANRESPONSE = DESCRIPTOR.message_types_by_name["ExecutePlanResponse"]
_EXECUTEPLANRESPONSE_ARROWBATCH = _EXECUTEPLANRESPONSE.nested_types_by_name["ArrowBatch"]
_EXECUTEPLANRESPONSE_METRICS = _EXECUTEPLANRESPONSE.nested_types_by_name["Metrics"]
_EXECUTEPLANRESPONSE_METRICS_METRICOBJECT = _EXECUTEPLANRESPONSE_METRICS.nested_types_by_name[
    "MetricObject"
]
_EXECUTEPLANRESPONSE_METRICS_METRICOBJECT_EXECUTIONMETRICSENTRY = (
    _EXECUTEPLANRESPONSE_METRICS_METRICOBJECT.nested_types_by_name["ExecutionMetricsEntry"]
)
_EXECUTEPLANRESPONSE_METRICS_METRICVALUE = _EXECUTEPLANRESPONSE_METRICS.nested_types_by_name[
    "MetricValue"
]
_EXPLAIN_EXPLAINMODE = _EXPLAIN.enum_types_by_name["ExplainMode"]
Plan = _reflection.GeneratedProtocolMessageType(
    "Plan",
    (_message.Message,),
    {
        "DESCRIPTOR": _PLAN,
        "__module__": "spark.connect.base_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Plan)
    },
)
_sym_db.RegisterMessage(Plan)

Explain = _reflection.GeneratedProtocolMessageType(
    "Explain",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXPLAIN,
        "__module__": "spark.connect.base_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Explain)
    },
)
_sym_db.RegisterMessage(Explain)

UserContext = _reflection.GeneratedProtocolMessageType(
    "UserContext",
    (_message.Message,),
    {
        "DESCRIPTOR": _USERCONTEXT,
        "__module__": "spark.connect.base_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.UserContext)
    },
)
_sym_db.RegisterMessage(UserContext)

AnalyzePlanRequest = _reflection.GeneratedProtocolMessageType(
    "AnalyzePlanRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _ANALYZEPLANREQUEST,
        "__module__": "spark.connect.base_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.AnalyzePlanRequest)
    },
)
_sym_db.RegisterMessage(AnalyzePlanRequest)

AnalyzePlanResponse = _reflection.GeneratedProtocolMessageType(
    "AnalyzePlanResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _ANALYZEPLANRESPONSE,
        "__module__": "spark.connect.base_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.AnalyzePlanResponse)
    },
)
_sym_db.RegisterMessage(AnalyzePlanResponse)

ExecutePlanRequest = _reflection.GeneratedProtocolMessageType(
    "ExecutePlanRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXECUTEPLANREQUEST,
        "__module__": "spark.connect.base_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.ExecutePlanRequest)
    },
)
_sym_db.RegisterMessage(ExecutePlanRequest)

ExecutePlanResponse = _reflection.GeneratedProtocolMessageType(
    "ExecutePlanResponse",
    (_message.Message,),
    {
        "ArrowBatch": _reflection.GeneratedProtocolMessageType(
            "ArrowBatch",
            (_message.Message,),
            {
                "DESCRIPTOR": _EXECUTEPLANRESPONSE_ARROWBATCH,
                "__module__": "spark.connect.base_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.ExecutePlanResponse.ArrowBatch)
            },
        ),
        "Metrics": _reflection.GeneratedProtocolMessageType(
            "Metrics",
            (_message.Message,),
            {
                "MetricObject": _reflection.GeneratedProtocolMessageType(
                    "MetricObject",
                    (_message.Message,),
                    {
                        "ExecutionMetricsEntry": _reflection.GeneratedProtocolMessageType(
                            "ExecutionMetricsEntry",
                            (_message.Message,),
                            {
                                "DESCRIPTOR": _EXECUTEPLANRESPONSE_METRICS_METRICOBJECT_EXECUTIONMETRICSENTRY,
                                "__module__": "spark.connect.base_pb2"
                                # @@protoc_insertion_point(class_scope:spark.connect.ExecutePlanResponse.Metrics.MetricObject.ExecutionMetricsEntry)
                            },
                        ),
                        "DESCRIPTOR": _EXECUTEPLANRESPONSE_METRICS_METRICOBJECT,
                        "__module__": "spark.connect.base_pb2"
                        # @@protoc_insertion_point(class_scope:spark.connect.ExecutePlanResponse.Metrics.MetricObject)
                    },
                ),
                "MetricValue": _reflection.GeneratedProtocolMessageType(
                    "MetricValue",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _EXECUTEPLANRESPONSE_METRICS_METRICVALUE,
                        "__module__": "spark.connect.base_pb2"
                        # @@protoc_insertion_point(class_scope:spark.connect.ExecutePlanResponse.Metrics.MetricValue)
                    },
                ),
                "DESCRIPTOR": _EXECUTEPLANRESPONSE_METRICS,
                "__module__": "spark.connect.base_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.ExecutePlanResponse.Metrics)
            },
        ),
        "DESCRIPTOR": _EXECUTEPLANRESPONSE,
        "__module__": "spark.connect.base_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.ExecutePlanResponse)
    },
)
_sym_db.RegisterMessage(ExecutePlanResponse)
_sym_db.RegisterMessage(ExecutePlanResponse.ArrowBatch)
_sym_db.RegisterMessage(ExecutePlanResponse.Metrics)
_sym_db.RegisterMessage(ExecutePlanResponse.Metrics.MetricObject)
_sym_db.RegisterMessage(ExecutePlanResponse.Metrics.MetricObject.ExecutionMetricsEntry)
_sym_db.RegisterMessage(ExecutePlanResponse.Metrics.MetricValue)

_SPARKCONNECTSERVICE = DESCRIPTOR.services_by_name["SparkConnectService"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\036org.apache.spark.connect.protoP\001"
    _EXECUTEPLANRESPONSE_METRICS_METRICOBJECT_EXECUTIONMETRICSENTRY._options = None
    _EXECUTEPLANRESPONSE_METRICS_METRICOBJECT_EXECUTIONMETRICSENTRY._serialized_options = b"8\001"
    _PLAN._serialized_start = 158
    _PLAN._serialized_end = 274
    _EXPLAIN._serialized_start = 277
    _EXPLAIN._serialized_end = 458
    _EXPLAIN_EXPLAINMODE._serialized_start = 359
    _EXPLAIN_EXPLAINMODE._serialized_end = 458
    _USERCONTEXT._serialized_start = 460
    _USERCONTEXT._serialized_end = 582
    _ANALYZEPLANREQUEST._serialized_start = 585
    _ANALYZEPLANREQUEST._serialized_end = 842
    _ANALYZEPLANRESPONSE._serialized_start = 845
    _ANALYZEPLANRESPONSE._serialized_end = 1111
    _EXECUTEPLANREQUEST._serialized_start = 1114
    _EXECUTEPLANREQUEST._serialized_end = 1321
    _EXECUTEPLANRESPONSE._serialized_start = 1324
    _EXECUTEPLANRESPONSE._serialized_end = 2107
    _EXECUTEPLANRESPONSE_ARROWBATCH._serialized_start = 1526
    _EXECUTEPLANRESPONSE_ARROWBATCH._serialized_end = 1587
    _EXECUTEPLANRESPONSE_METRICS._serialized_start = 1590
    _EXECUTEPLANRESPONSE_METRICS._serialized_end = 2107
    _EXECUTEPLANRESPONSE_METRICS_METRICOBJECT._serialized_start = 1685
    _EXECUTEPLANRESPONSE_METRICS_METRICOBJECT._serialized_end = 2017
    _EXECUTEPLANRESPONSE_METRICS_METRICOBJECT_EXECUTIONMETRICSENTRY._serialized_start = 1894
    _EXECUTEPLANRESPONSE_METRICS_METRICOBJECT_EXECUTIONMETRICSENTRY._serialized_end = 2017
    _EXECUTEPLANRESPONSE_METRICS_METRICVALUE._serialized_start = 2019
    _EXECUTEPLANRESPONSE_METRICS_METRICVALUE._serialized_end = 2107
    _SPARKCONNECTSERVICE._serialized_start = 2110
    _SPARKCONNECTSERVICE._serialized_end = 2309
# @@protoc_insertion_point(module_scope)
