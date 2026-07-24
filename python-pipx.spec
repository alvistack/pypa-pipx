# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-pipx
Epoch: 100
Version: 1.16.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Install and run Python applications in isolated environments
License: MIT
URL: https://github.com/pypa/pipx/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
pipx is a tool to help you install and run end-user applications written
in Python. It’s roughly similar to macOS’s brew, JavaScript’s npx, and
Linux’s apt.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} >= 1500
%package -n python%{python3_version_nodots}-pipx
Summary: Install and run Python applications in isolated environments
Requires: python3
Requires: python3-argcomplete >= 1.9.4
Requires: python3-filelock >= 3.16
Requires: python3-packaging >= 20.0
Requires: python3-platformdirs >= 4.6
Requires: python3-tomli
Requires: python3-userpath >= 1.6.0
Provides: pipx = %{epoch}:%{version}-%{release}
Provides: python3-pipx = %{epoch}:%{version}-%{release}
Provides: python3dist(pipx) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pipx = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pipx) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pipx = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pipx) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pipx
pipx is a tool to help you install and run end-user applications written
in Python. It’s roughly similar to macOS’s brew, JavaScript’s npx, and
Linux’s apt.

%files -n python%{python3_version_nodots}-pipx
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} >= 1500)
%package -n pipx
Summary: Install and run Python applications in isolated environments
Requires: python3
Requires: python3-argcomplete >= 1.9.4
Requires: python3-filelock >= 3.16
Requires: python3-packaging >= 20.0
Requires: python3-platformdirs >= 4.6
Requires: python3-tomli
Requires: python3-userpath >= 1.6.0
Provides: pipx = %{epoch}:%{version}-%{release}
Provides: python3-pipx = %{epoch}:%{version}-%{release}
Provides: python3dist(pipx) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pipx = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pipx) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pipx = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pipx) = %{epoch}:%{version}-%{release}

%description -n pipx
pipx is a tool to help you install and run end-user applications written
in Python. It’s roughly similar to macOS’s brew, JavaScript’s npx, and
Linux’s apt.

%files -n pipx
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
